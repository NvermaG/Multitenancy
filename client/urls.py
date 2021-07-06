from django.urls import path
from .views import ClientView

urlpatterns = [
    path('client/', ClientView.as_view({'get': 'list'})),
    path('client/post', ClientView.as_view({'post': 'create'}))
]