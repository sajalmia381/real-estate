from django.utils.text import slugify
from django.utils.crypto import get_random_string


def get_generate_slug(instance, new_slug=None):
    if new_slug is not None:
        slug = new_slug
    else:
        try:
            slug = slugify(instance.title)
        except AttributeError:
            slug = slugify(instance.name)
    Klass = instance.__class__
    qs_exists = Klass.objects.filter(slug=slug).exists()
    if qs_exists:
        new_slug = f'{slug}-{get_random_string()}'
        return new_slug
    return slug
