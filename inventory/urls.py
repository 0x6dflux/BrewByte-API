from rest_framework.routers import SimpleRouter

from inventory.views import (
    CategoryViewSet,
    IngredientViewSet,
    PictureViewSet,
    ProductViewSet,
)

router = SimpleRouter(use_regex_path=False)
router.register("category", CategoryViewSet, "category")
router.register("ingredient", IngredientViewSet, "ingredient")
router.register("product-picture", PictureViewSet, "picture")
router.register("product", ProductViewSet, "product")

app_name = "inventory"
urlpatterns = router.urls
