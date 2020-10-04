from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import ArticleViewSetModel

router = DefaultRouter()
router.register("articles", ArticleViewSetModel, basename="articles")

urlpatterns = [
    path('viewset/', include(router.urls)),
]
