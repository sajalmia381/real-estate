from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from rest_framework import generics, status
from rest_framework.permissions import AllowAny, IsAuthenticated
from django_filters import rest_framework as filters
from rest_framework.views import APIView

from .filters import ListingFilter
from .models import Listing
from .serializers import ListingListSerializer, ListingDetailsSerializer, ListingCreateSerializer


class ListingPagination(PageNumberPagination):
    page_size = 12
    page_size_query_param = 'page_size'
    max_page_size = 1000


class ListingListView(generics.ListAPIView):
    queryset = Listing.objects.filter(is_published=True).order_by('-created_at')
    pagination_class = ListingPagination
    serializer_class = ListingListSerializer
    permission_classes = (AllowAny,)
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = ListingFilter


class ListingDetailsView(generics.RetrieveAPIView):
    queryset = Listing.objects.filter(is_published=True)
    serializer_class = ListingDetailsSerializer
    permission_classes = (AllowAny,)
    lookup_field = 'slug'


class ListingCreateView(generics.CreateAPIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request, *args, **kwargs):
        serializer = ListingCreateSerializer(data=self.request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)