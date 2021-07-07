from django.db import models
from django_tenants.models import TenantMixin, DomainMixin
from rest_framework.response import Response


class Client(TenantMixin):
    name = models.CharField(max_length=100)

    # default true, schema will be automatically created and synced when it is saved
    auto_drop_schema = True
    auto_create_schema = True

    def __str__(self):
        return self.name


class Domain(DomainMixin):
    pass
