from django import template
from django.conf import settings
from pathlib import Path
from PIL import Image
import os

register = template.Library()


def _make_thumb(src_path: Path, dst_path: Path, size=(600, 420)):
    # create thumbnail directory if needed
    dst_path.parent.mkdir(parents=True, exist_ok=True)
    try:
        with Image.open(src_path) as im:
            im = im.convert('RGB')
            im.thumbnail(size, Image.LANCZOS)
            im.save(dst_path, format='JPEG', quality=85)
            return True
    except Exception:
        return False


@register.filter(name='thumb')
def thumb(image_field, kind='card'):
    """
    Returns URL to a thumbnail for an ImageField file. If thumbnail doesn't
    exist it will be created. `kind` can be 'card' or 'carousel' to choose size.
    """
    if not image_field:
        return ''

    rel_path = image_field.name  # e.g. 'pacotes/disney.jpeg'
    base, ext = os.path.splitext(rel_path)
    if kind == 'carousel':
        suffix = '_carousel'
        size = (1200, 420)
    else:
        suffix = '_thumb'
        size = (800, 420)  # wide thumb to keep good quality

    thumb_rel = f"{base}{suffix}.jpg"
    media_root = Path(settings.MEDIA_ROOT)
    src_path = media_root / rel_path
    dst_path = media_root / thumb_rel

    # If thumb exists, return URL immediately
    if dst_path.exists():
        return settings.MEDIA_URL + thumb_rel.replace('\\', '/')

    # If source exists, try to create thumb
    if src_path.exists():
        created = _make_thumb(src_path, dst_path, size=size)
        if created:
            return settings.MEDIA_URL + thumb_rel.replace('\\', '/')

    # Fallback to original url
    try:
        return image_field.url
    except Exception:
        return ''
