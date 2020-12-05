from rest_framework import serializers

from .models import Listing


class ListingListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Listing
        fields = '__all__'


class ListingDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Listing
        fields = '__all__'


class ListingCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Listing
        fields = ('title', 'image', 'description', 'price', 'sale_type', 'bed_room', 'bath_room', 'square_feet', 'address', 'city', 'state', 'zip_code')

