from .models import HotelBooking
from rest_framework import serializers


class HotelSerializer(serializers.ModelSerializer):
    class Meta:
        model = HotelBooking
        fields = '__all__'
