import string
import random
from django.utils.text import slugify

def generator(size=10,chars=string.ascii_letters + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))

def kreye_slug(instance, field_name, new_slug=None):
    if new_slug is not None:
        slug = new_slug[:100]
    else:
        slug = slugify(getattr(instance,field_name))[:70] # params : Title or Name or Subject
        if not slug:
            slug = generator(10)
    Klass = instance.__class__
    qs_exists = Klass.objects.filter(slug=slug).exists()
    if qs_exists:
        new_slug = "%s-%s" % (slug,generator(4))
        if len(new_slug) > 100:
            new_slug = new_slug[:100]
        return kreye_slug(instance,field_name, new_slug)
    return slug