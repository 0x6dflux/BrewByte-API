from django.urls import path

from inventory.views import (
    CategoryListCreateAPIView,
    CategoryRetrieveUpdateDestroyAPIView,
    IngredientListCreateAPIView,
    IngredientRetrieveUpdateDestroyAPIView,
    PictureListCreateAPIView,
    PictureRetrieveUpdateDestroyAPIView,
    ProductListCreateAPIView,
    ProductRetrieveUpdateDestroyAPIView,
)

app_name = "inventory"
urlpatterns = [
    path("category/", CategoryListCreateAPIView.as_view(), name="category"),
    path(
        "category/<int:pk>/",
        CategoryRetrieveUpdateDestroyAPIView.as_view(),
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
