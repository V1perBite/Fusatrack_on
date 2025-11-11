from django.urls import include, path
from rest_framework.routers import DefaultRouter
from . import views
from .views import RouteViewSet, StopViewSet

urlpatterns = [
    path('test/', views.test, name='test'),
    path('routes/', views.RouteListAPIView.as_view(), name='routes-list'),
    path('stops/', views.StopListAPIView.as_view(), name='stops-list'),
]

router = DefaultRouter()
router.register(r'routes', RouteViewSet)
router.register(r'stops', StopViewSet)

urlpatterns = [
    path('', include(router.urls)),
]