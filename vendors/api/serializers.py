from rest_framework import serializers
from vendors.models import Vendor

class VendorSerializer(serializers.Serializer):
    id=serializers.IntegerField()
    name=serializers.CharField(max_length=10)
    contact_details=serializers.TextField()
    address=serializers.TextField()
    vendor_code=serializers.CharField(unique=True,max_length=20)
    on_time_delivery_rate=serializers.FloatField()
    quality_rating_avg=serializers.FloatField()
    average_response_time=serializers.FloatField()
    fulfillment_rate=serializers.FloatField()


    def create(self,validated_data):
        return Vendor.objects.create(**validated_data)