from django.urls import path

from .views import CommentAdd, CommentView

app_name = "comments"

urlpatterns = [
    path('comment-add/', CommentAdd.as_view(), name='comment-add'),
    path('comment-view/<int:pk>/', CommentView.as_view(), name='comment-view')
]
