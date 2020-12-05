from django.urls import path

from .views import ListingListView, ListingDetailsView, ListingCreateView

urlpatterns = [
    path('listings', ListingListView.as_view(), name='api_listings'),
    path('listings/create', ListingCreateView.as_view(), name='api_listing_create'),
    path('listings/<slug:slug>', ListingDetailsView.as_view(), name='api_listing_details'),
]