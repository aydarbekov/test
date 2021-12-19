from webapp.models import Client
from rest_framework import serializers


class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client

        fields = (
            'identity_number', 'mobile_phone', 'additional_numbers', 'last_name', 'first_name', 'middle_name', 'emails',
            'created_at', 'updated_at',
            'status_updated', 'is_active', 'client_type', 'sex', 'timezone', 'departments', 'social_medias'
        )

