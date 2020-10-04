from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import ArticleGenericAPIView, ArticleViewSet

router = DefaultRouter()
router.register("articles", ArticleViewSet, basename="articles")

urlpatterns = [
    # path("article/<int:id>", ArticleGenericAPIView.as_view()),
    # path("articles/", ArticleGenericAPIView.as_view()),
    path('viewset/', include(router.urls)),
    path('viewset/<int:pk>/', include(router.urls)),
]
