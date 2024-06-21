from django.urls import path

from . import views

app_name = "forum"
urlpatterns = [
    # # ex: /polls/
    # path("", views.index, name="index"),
    # # ex: /polls/5/
    # path("<int:topic_id>/", views.detail, name="detail"),
    # # ex: /polls/5/commentsection/
    # path("<int:topic_id>/commentsection/", views.commentsection, name="commentsection"),
    path("", views.IndexView.as_view(), name="index"),
    path("<int:pk>/", views.DetailView.as_view(), name="detail"),
    path("<int:pk>/commentsection/", views.CommentSection.as_view(), name="commentsection"),
    # ex: /polls/5/comment/
    path("<int:topic_id>/likecomment/", views.likecomment, name="likecomment"),
]