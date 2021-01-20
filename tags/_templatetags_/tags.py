from django import template
from django.contrib.contenttypes.models import ContentType
from .models import Tag

template.Library()

register = template.Library()


""" @register.inclusion_tag('tags/tags.html', takes_context=True)
def tags(context, obj, next="/"):
    ct = ContentType.objects.get_for_model(obj)
    tags = Tag.objects.filter(
        content_type=ct,
        object_id=obj.pk
    )
    return {
        'ct': ct.pk,
        'obj_id': obj.pk,
        'tags': tags,
        'next': next,
    }
 """