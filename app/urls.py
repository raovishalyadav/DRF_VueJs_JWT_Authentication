from django.urls import path, include
from .views import cruddata
from rest_framework import routers


router = routers.DefaultRouter()

# to view data
router.register("CRUD", cruddata)

urlpatterns = [
    path("", include(router.urls)),
]
