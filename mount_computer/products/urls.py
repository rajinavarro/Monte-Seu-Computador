from django.urls import include, path
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'products/cpu', views.CpuViewSet)
router.register(r'products/motherboard', views.MotherboardViewSet)
router.register(r'products/ram-memory', views.RamMemoryViewSet)
router.register(r'products/video-card', views.VideoCardViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]