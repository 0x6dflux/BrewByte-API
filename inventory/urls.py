# type: ignore

from django.urls import path

from inventory.views import (
    CategoryViewSet,
    IngredientViewSet,
    PictureViewSet,
    ProductViewSet,
)

action_without_detail = {"get": "list", "post": "create"}
action_with_detail = {
    "get": "retrieve",
    "put": "update",
    "patch": "partial_update",
    "delete": "destroy",
}

app_name = "inventory"
urlpatterns = [
    path(
        "category/",
        CategoryViewSet.as_view(action_without_detail),
        name="category",
    ),
    path(
        "category/<int:pk>/",
        CategoryViewSet.as_view(action_with_detail),
        name="category-detail",
    ),
    path(
        "ingredient/",
        IngredientViewSet.as_view(action_without_detail),
        name="ingredient",
    ),
    path(
        "ingredient/<int:pk>/",
        IngredientViewSet.as_view(action_with_detail),
        name="ingredient-detail",
    ),
    path(
        "product/",
        ProductViewSet.as_view(action_without_detail),
        name="product",
    ),
    path(
        "product/<int:pk>/",
        ProductViewSet.as_view(action_with_detail),
        name="product-detail",
    ),
    path(
        "product-picture/",
        PictureViewSet.as_view(action_without_detail),
        name="product-picture",
    ),
    path(
        "product-picture/<int:pk>/",
        PictureViewSet.as_view(action_with_detail),
        name="product-picture-detail",
    ),
]
