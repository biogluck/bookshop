from django.shortcuts import render
from django.views.generic import DetailView
from django.views.generic.base import RedirectView
from django.contrib.contenttypes.models import ContentType
from django.contrib import messages


from .models import Comment


class CommentAdd(RedirectView):

    def get_redirect_url(self, *args, **kwargs):
        next = self.request.POST.get('next', '/')
        ct_id = self.request.POST.get('ct_id')
        obj_id = self.request.POST.get('obj_id')
        comment = self.request.POST.get('comment')
        usr = self.request.user
        if ct_id and obj_id and comment:
            ct = ContentType.objects.get_for_id(ct_id)
            comment = Comment.objects.create(
                comment=comment,
                content_type=ct,
                object_id=obj_id,
                commentator=usr,
                # defaults={
                #     'comment': comment,
                #     'content_type': ct,
                #     'object_id': obj_id,
                # }
            )
        # else:
        #     pass
        # if created:
        message_text = "Done"
        extra_tags = 'alert-success'
        # else:
        #     message_text = "not"
        #     extra_tags = 'alert-warning'
        messages.add_message(
            self.request,
            messages.INFO,
            message_text,
            extra_tags=extra_tags)

        return next


class CommentView(DetailView):
    model = Comment
    template_name = "comments/comment-view.html"

    def get_context_data(self, **kwargs):
        context = super(CommentView, self).get_context_data(**kwargs)
        context['comments'] = Comment.objects.filter(
            comment=self.object.comment
        )
        return context
