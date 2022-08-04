from rest_framework import serializers
from .models import Booktmodel

class Serializer(serializers.ModelSerializer):
    class Meta:
        model = Booktmodel
        fields = ['id', 'Name', 'writer', 'publication', 'status']