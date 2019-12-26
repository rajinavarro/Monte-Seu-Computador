from django.urls import include, path
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register('',views.OrderViewSet, basename='Order')

urlpatterns = [
    path('api/', include(router.urls)),
    path(r'order-add/', views.add_order),
]