from django.urls import include, path
from rest_framework import routers
from . import views

router = routers.DefaultRouter()

router.register(r'cpu', views.CpuViewSet, basename='cpu')
router.register(r'motherboard', views.MotherboardViewSet)
router.register(r'ram-memory', views.RamMemoryViewSet)
router.register(r'video-card', views.VideoCardViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
    path(r'',views.products_list),
    path(r'cpu-list/', views.cpu_list),
    path(r'motherboard-list/', views.motherboard_list),
    path(r'videocard-list/', views.videocard_list),
    path(r'rammemory-list/', views.rammemory_list),
    path(r'cpu-add/', views.add_cpu),
    path(r'motherboard-add/', views.add_motherboard),
    path(r'videocard-add/', views.add_videocard),
    path(r'rammemory-add/', views.add_rammemory),
]