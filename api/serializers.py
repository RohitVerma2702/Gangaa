from rest_framework import serializers
from .models import Store

class StoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Store
        fields = ('id', 'district', 'block', 'gram_panchayat', 'village', 'store_type', 'store_name', 'owner_name', 'contact_number', 'pincode', 'products', 'delivery_area', 'delivery_status', 'remark')