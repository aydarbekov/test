from webapp.models import Client, LegalEntity, Department
from rest_framework import serializers


class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client

        fields = (
            'identity_number', 'mobile_phone', 'additional_numbers', 'last_name', 'first_name', 'middle_name', 'emails',
            'created_at', 'updated_at',
            'status_updated', 'is_active', 'client_type', 'sex', 'timezone', 'departments', 'social_medias'
        )


class DepartmentSerializer(serializers.ModelSerializer):
    clients = ClientSerializer(many=True, read_only=True)

    class Meta:
        model = Department

        fields = (
            'identity_number', 'name', 'parent', 'clients'
        )


class LegalEntitySerializer(serializers.ModelSerializer):
    departments = DepartmentSerializer(many=True, read_only=True)


    class Meta:
        model = LegalEntity

        fields = (
            'identity_number', 'created_at', 'updated_at',
            'full_name', 'short_name', 'inn', 'kpp', 'departments'
        )
