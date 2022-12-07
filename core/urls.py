from django.urls import path, include
from core import views as _v
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('products', _v.ProductViewSet)
router.register('variants', _v.VariantViewSet)
router.register('images', _v.ImageViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
