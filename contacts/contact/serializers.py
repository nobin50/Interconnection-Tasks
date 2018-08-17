from rest_framework import serializers
from .models import Contact_List


class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'name',
            'phone',
            'district',
        )
        model = Contact_List