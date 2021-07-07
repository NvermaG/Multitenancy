from django.db import transaction
from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .serializers import ClientSerializer
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from django_tenants.models import TenantMixin, DomainMixin
from .models import Client, Domain
# Create your views here.


class ClientView(ModelViewSet):
    serializer_class = ClientSerializer
    permission_classes = (AllowAny, )
    queryset = Client.objects.all()
    http_method_names = ['get', 'post', 'patch', 'put', 'delete']


    @transaction.atomic
    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid()
        tenant = Client(schema_name=serializer.data.get('schema_name'),
                        name=serializer.data.get('name'))
        tenant.save()
        domain = Domain()
        domain.domain = str(serializer.data.get('name'))+".localhost"
        domain.tenant = tenant
        domain.is_primary = True
        domain.save()
        return Response("Tenant created successfully")

    def list(self, request, *args, **kwargs):
        obj = self.get_queryset()
        serializer = self.get_serializer(obj, many=True)
        return Response(serializer.data)

    def delete(self):
        instance = self.get_object()
        instance.delete()
        return Response("Deleted")

    @transaction.atomic
    def update(self, request, *args, **kwargs):
        obj = self.get_object()
        serializer = self.get_serializer(obj, data=request.data)
        serializer.is_valid()
        serializer.save()
        return Response("Update successfully")
