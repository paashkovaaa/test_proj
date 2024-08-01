import random

from django.http import JsonResponse
from rest_framework import generics, mixins
from rest_framework.decorators import api_view

from .models import Phrase
from .serializers import PhraseSerializer


from django.shortcuts import render


def index(request):
    return render(request, "index.html")


@api_view(["GET"])
def get_random_phrase(request):
    phrases = Phrase.objects.all()
    if phrases.exists():
        phrase = random.choice(phrases)
        serializer = PhraseSerializer(phrase)
        return JsonResponse(serializer.data)
    return JsonResponse({"error": "No phrases found"}, status=404)
