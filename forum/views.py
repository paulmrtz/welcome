from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.shortcuts import get_object_or_404, render
from django.db.models import F
from django.urls import reverse
from django.views import generic
from .models import Topic, Comment


# def index(request):
#     latest_topic_list = Topic.objects.order_by("-pub_date")[:5]
#     context = {
#         "latest_topic_list": latest_topic_list,
#     }
#     return render(request, "forum/index.html", context)


# def detail(request, topic_id):
#     topic = get_object_or_404(Topic, pk=topic_id)
#     return render(request, "forum/detail.html", {"topic": topic})


# def commentsection(request, topic_id):
#     topic = get_object_or_404(Topic, pk=topic_id)
#     return render(request, "forum/commentsection.html", {"topic": topic})

class IndexView(generic.ListView):
    template_name = "forum/index.html"
    context_object_name = "latest_topic_list"

    def get_queryset(self):
        """Return the last five published topics."""
        return Topic.objects.order_by("-pub_date")[:5]


class DetailView(generic.DetailView):
    model = Topic
    template_name = "forum/detail.html"


class CommentSection(generic.DetailView):
    model = Topic
    template_name = "forum/commentsection.html"


def likecomment(request, topic_id):
    topic = get_object_or_404(Topic, pk=topic_id)
    try:
        selected_comment = topic.comment_set.get(pk=request.POST["comment"])
    except (KeyError, Comment.DoesNotExist):
        # Redisplay the topic voting form.
        return render(
            request,
            "forum/detail.html",
            {
                "topic": topic,
                "error_message": "You didn't select a comment.",
            },
        )
    else:
        selected_comment.likes = F("likes") + 1
        selected_comment.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse("forum:commentsection", args=(topic.id,)))