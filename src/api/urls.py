from django.conf.urls import url, patterns, include
from .views import UserViewSet, MovieViewSet
from rest_framework.routers import DefaultRouter


# Create a router and register the viewsets with it
router = DefaultRouter()
router.register(r'movies', MovieViewSet)
router.register(r'users', UserViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
]
