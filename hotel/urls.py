from django.urls import path
from .views import HotelView

urlpatterns = [
    path('hotel/', HotelView.as_view({'get': 'get'})),
    path('hotel/post', HotelView.as_view({'post': 'post'})),
    path('<int:pk>/hotel/delete', HotelView.as_view({'delete': 'destroy'})),
    path('<int:pk>/hotel/update', HotelView.as_view({'patch': 'update'}))
]