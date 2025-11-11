from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import RouteViewSet, StopViewSet

router = DefaultRouter()
router.register(r'routes', RouteViewSet)
router.register(r'stops', StopViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
]
