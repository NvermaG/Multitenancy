from django.shortcuts import render
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from .models import VillaBooking
from .serializers import VillaSerializer
from django.db import transaction

# Create your views here.


class VillaView(ModelViewSet):
    serializer_class = VillaSerializer
    permission_classes = (AllowAny,)
    queryset = VillaBooking.objects.all()
    http_method_names = ['get', 'post', 'patch', 'put', 'delete']

    @transaction.atomic()
    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid()
        self.perform_create(serializer)
        return Response(serializer.data)

    def get(self, request, *args, **kwargs):
        obj = self.get_queryset()
        serializer = self.get_serializer(obj, many=True)
        return Response(serializer.data)

    def update(self, request, *args, **kwargs):
        obj = self.get_object()
        serializer = self.get_serializer(obj, data=request.data)
        serializer.is_valid()
        self.perform_update(serializer)
        return Response("Update successfully")

