from django.shortcuts import render

from rest_framework import viewsets

from webapp.models import Client, LegalEntity, Department
from webapp.serializers import ClientSerializer, LegalEntitySerializer, DepartmentSerializer


class ClientViewSet(viewsets.ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer


class LegalEntityViewSet(viewsets.ModelViewSet):
    queryset = LegalEntity.objects.all()
    serializer_class = LegalEntitySerializer


class DepartmentSerializerViewSet(viewsets.ModelViewSet):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer
