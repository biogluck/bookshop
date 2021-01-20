from django import template
from django.contrib.contenttypes.models import ContentType
from comments.models import Comment
from django.contrib.auth import get_user_model


register = template.Library()
User = get_user_model()


@register.inclusion_tag('comments/comment-form.html', takes_context=True)
def comments(context, obj, next="/"):
    ct = ContentType.objects.get_for_model(obj)
    # print('context: ', context)
    usr = User.objects.get(username=context['user'])
    # print('usr: ', usr)
    comments = Comment.objects.filter(
        content_type=ct,
        object_id=obj.pk
    )
    return {
        'ct_id': ct.pk,
        'obj_id': obj.pk,
        'comments': comments,
        'next': next,
        'comments_count': len(comments),
        'usr': usr,
    }
