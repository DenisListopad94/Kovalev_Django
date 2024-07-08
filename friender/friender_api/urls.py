from django.urls import path
from .views import HotelOwnerListView, HotelOwnerDetailView, HobbiesListView
from rest_framework.urlpatterns import format_suffix_patterns


urlpatterns = [
    path('hotel_owners/', HotelOwnerListView.as_view(), name='hotel_owner_list'),
    path('hotel_owners/<int:pk>/', HotelOwnerDetailView.as_view(), name='hotel_owner_detail'),
    path('hobbies/', HobbiesListView.as_view(), name='hobbies_list'),
]

urlpatterns = format_suffix_patterns(urlpatterns)