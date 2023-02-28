from .models import Word
from django.http import JsonResponse
from django.core import serializers


def index(request):
    my_model_data = Word.objects.all()
    serialized_data = serializers.serialize('json', my_model_data)
    return JsonResponse(serialized_data, safe=False)


def word(request, word):
    my_model_data = Word.objects.get(word_text=word)
    word_object = Word.objects.filter(pk=my_model_data.pk)
    serialized_data = serializers.serialize('json', word_object)
    return JsonResponse(serialized_data, safe=False)
