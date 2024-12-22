from django.urls import path

from catalog.views import CatalogView, ItemView

app_name = "catalog"

urlpatterns = [
    path("", CatalogView.as_view(), name="catalog"),
    path("film/<int:pk>", ItemView.as_view(), name="item"),
]
