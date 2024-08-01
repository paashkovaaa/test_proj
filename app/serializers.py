from rest_framework import serializers

from app.models import Phrase


class PhraseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Phrase
        fields = ["text"]
