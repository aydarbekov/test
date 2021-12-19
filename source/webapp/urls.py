from django.urls import include, path

from rest_framework import routers

from webapp import views

router = routers.DefaultRouter()

router.register(r'clients', views.ClientViewSet)
router.register(r'legalentity', views.LegalEntityViewSet)

app_name = 'webapp'

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))

]
