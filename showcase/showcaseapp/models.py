from django.db import models
from django.db.models.signals import pre_save
from django.dispatch import receiver
import openai
import environ


class Language(models.Model):
    language_title = models.CharField(max_length=100)

    def __str__(self):
        return self.language_title


class Word(models.Model):
    language = models.ForeignKey(Language, on_delete=models.CASCADE)
    word_text = models.CharField(max_length=100)
    example_usage = models.CharField(max_length=500)

    def __str__(self):
        return self.word_text


@receiver(pre_save, sender=Word)
def get_example(sender, instance, **kwargs):
    env = environ.Env()
    openai.api_key = env('OPENAI_API_KEY')
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=f"Return one usage example of word {instance.word_text} in one sentence without any other text.",
        max_tokens=100,
        temperature=0
    )
    instance.example_usage = response.choices[0].text.strip()
