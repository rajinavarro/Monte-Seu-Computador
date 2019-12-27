from django.urls import include, path
from rest_framework import routers
from . import views

router = routers.DefaultRouter()

router.register(r'cpu', views.CpuViewSet)
router.register(r'motherboard', views.MotherboardViewSet)
router.register(r'ram-memory', views.RamMemoryViewSet)
router.register(r'video-card', views.VideoCardViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
]