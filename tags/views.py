from django.shortcuts import render
from django.views.generic.base import RedirectView
from django.contrib.contenttypes.models import ContentType

from .models import Tag

from django.contrib import messages


class TagAdd(RedirectView):
    def get_redirect_url(self, *args, **kwargs):
        next = self.request.POST.get('next', '/')
        ct_id = ....ct_id
        obj_id
        tag = self.request.POST.get('tag')
        if ct_id and obj_id and tag:
            ct = ContentType.objects.get_for_id(ct_id)
            tag, created = Tag.objects.get_or_create(
                tag=tag,
                content_type=ct,
                object_id=obj_id,
                defaults={
                    'tag': tag,
                    'content_type': ct,
                    'object_id': obj_id,
                }
            )
            if created:
                message_text = "x"
                extra_tags = 'alert-success'
            else:
                message_text = "not"
                extra_tags = 'alert-warning'
            messages.add_message(
                self.request,
                messages.INFO,
                message_text,
                extra_tags=extra_tags)
        return next


class TagView(DetailView):
    model = Tag

    def def get_context_data(self, **kwargs):
        context = super(TagView, self).get_context_data(**kwargs)
        context['tags'] = Tag.objects.filter(
            tag=self.object.tag
        )
        return context
