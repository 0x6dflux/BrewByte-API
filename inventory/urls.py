from django.urls import path

from inventory.views import (
    IngredientListCreateAPIView,
    IngredientRetrieveUpdateDestroyAPIView,
    PictureListCreateAPIView,
    PictureRetrieveUpdateDestroyAPIView,
    ProductListCreateAPIView,
    ProductRetrieveUpdateDestroyAPIView,
    category_list_create,
    category_retrieve_update_destroy,
)

app_name = "inventory"
urlpatterns = [
    path("category/", category_list_create, name="category"),
    path(
        "category/<int:pk>/",
        category_retrieve_update_destroy,
        name="category-detail",
    ),
    path("ingredient/", IngredientListCreateAPIView.as_view(), name="ingredient"),
    path(
        "ingredient/<int:pk>/",
        IngredientRetrieveUpdateDestroyAPIView.as_view(),
        name="ingredient-detail",
    ),
    path("product/", ProductListCreateAPIView.as_view(), name="product"),
    path(
        "product/<int:pk>/",
        ProductRetrieveUpdateDestroyAPIView.as_view(),
        name="product-detail",
    ),
    path(
        "product-picture/",
        PictureListCreateAPIView.as_view(),
        name="product-picture",
    ),
    path(
        "product-picture/<int:pk>/",
        PictureRetrieveUpdateDestroyAPIView.as_view(),
        name="product-picture-detail",
    ),
]
