from django.test import TestCase
from django.http import JsonResponse
from showcaseapp.models import Word, Language
from django.urls import reverse


class WordTestCase(TestCase):
    def setUp(self):
        Language.objects.create(language_title="English")
        Word.objects.create(word_text="raucous", language=Language.objects.get(language_title="English"))

    def test_get_examples(self):
        raucous = Word.objects.get(word_text="raucous")
        example = "The raucous crowd cheered loudly for the winning team."
        self.assertEqual(raucous.example_usage, example)


class WordViewTests(TestCase):
    def setUp(self):
        Language.objects.create(language_title="English")
        Word.objects.create(word_text="raucous", language=Language.objects.get(language_title="English"))

    def test_returns_JSON(self):
        url = reverse('showcaseapp:word', args=["raucous"])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertIs(isinstance(response, JsonResponse), True)
