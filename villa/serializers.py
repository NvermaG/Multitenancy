from rest_framework import serializers
from .models import VillaBooking


class VillaSerializer(serializers.ModelSerializer):
    class Meta:
        model = VillaBooking
        fields = '__all__'
