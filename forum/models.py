import datetime

from django.db import models
from django.utils import timezone
from django.contrib import admin


class Topic(models.Model):
    topic_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField("date published")
    def __str__(self):
        return self.topic_text
    @admin.display(
        boolean=True,
        ordering="pub_date",
        description="Published recently?",
    )
    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now


class Comment(models.Model):
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    comment_text = models.CharField(max_length=200)
    likes = models.IntegerField(default=0)
    def __str__(self):
        return self.comment_text