from django.urls import path
from .views import VillaView

urlpatterns = [
    path('villa/', VillaView.as_view({'get': 'get'})),
    path('villa/post', VillaView.as_view({'post': 'post'})),
    path('<int:pk>/villa/delete', VillaView.as_view({'delete': 'destroy'})),
    path('<int:pk>/villa/update', VillaView.as_view({'patch': 'update'}))
]
