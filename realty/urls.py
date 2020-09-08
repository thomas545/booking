from django.urls import path, include
from rest_framework import routers
from . import views, viewsets

router = routers.DefaultRouter()

router.register("realty", viewsets.RealityViewSet, basename="realty")


urlpatterns = [
    path("categories/", views.CategoryView.as_view(), name="categories"),
    path("bulk/categories/", views.BulkCategoryView.as_view(), name="bulk_categories"),
]
