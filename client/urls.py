from django.urls import path
from .views import ClientView

urlpatterns = [
    path('client/', ClientView.as_view({'get': 'list'})),
    path('client/post', ClientView.as_view({'post': 'post'})),
    path('<int:pk>/client/delete', ClientView.as_view({'post': 'delete'})),
    path('<int:pk>/client/update', ClientView.as_view({'patch': 'update'}))
]