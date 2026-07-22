from django.urls import path

from inventory.views import ProductViewSet

app_name = "inventory"
urlpatterns = [
    path("product/", ProductViewSet.as_view()),
]
