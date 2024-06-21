from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")


def detail(request, topic_id):
    return HttpResponse("You're looking at topic %s." % topic_id)


def comments(request, topic_id):
    response = "You're looking at the results of topic %s."
    return HttpResponse(response % topic_id)


def comment(request, topic_id):
    return HttpResponse("You're commenting on topic %s." % topic_id)