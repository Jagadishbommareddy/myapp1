
from django.conf.urls import include, url
from django.contrib import admin
from rest_framework import routers
from taskapp.views import CustomerViewSet
from taskapp.views import AddressViewSet
router = routers.DefaultRouter()
router.register(r'customers',CustomerViewSet)
router.register(r'addres',AddressViewSet)

urlpatterns = [
    url(r'^',include(router.urls)),
    url(r'^admin/', include(admin.site.urls)),
]
