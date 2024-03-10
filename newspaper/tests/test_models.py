from django.test import TestCase
from newspaper.models import Redactor, Topic, Newspaper
from datetime import date


class ModelTestCase(TestCase):
    def setUp(self):
        self.redactor = Redactor.objects.create_user(
            username="redactor1",
            first_name="John",
            last_name="Doe",
            email="john.doe@example.com",
            years_of_experience=5,
        )
        self.topic = Topic.objects.create(name="Politics")
        self.newspaper = Newspaper.objects.create(
            title="Breaking News",
            content="Lorem ipsum dolor sit amet",
        )
        self.newspaper.topics.add(self.topic)
        self.newspaper.publishers.add(self.redactor)

    def test_redactor_str(self):
        self.assertEqual(str(self.redactor), "redactor1 (John Doe)")

    def test_topic_str(self):
        self.assertEqual(str(self.topic), "Politics")

    def test_newspaper_str(self):
        self.assertEqual(str(self.newspaper), "Breaking News")

    def test_newspaper_topics(self):
        self.assertIn(self.topic, self.newspaper.topics.all())

    def test_newspaper_publishers(self):
        self.assertIn(self.redactor, self.newspaper.publishers.all())

    def test_newspaper_published_date(self):
        self.assertEqual(self.newspaper.published_date, date.today())
