import datetime

from django.test import TestCase
from django.utils import timezone

from .models import Topic


class TopicModelTests(TestCase):
    def test_was_published_recently_with_future_topic(self):
        """
        was_published_recently() returns False for topics whose pub_date
        is in the future.
        """
        time = timezone.now() + datetime.timedelta(days=30)
        future_topic = Topic(pub_date=time)
        self.assertIs(future_topic.was_published_recently(), False)