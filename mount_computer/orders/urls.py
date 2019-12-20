from django.urls import include, path
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register('all',views.OrderViewSet)



urlpatterns = [
    path('', include(router.urls)),
]