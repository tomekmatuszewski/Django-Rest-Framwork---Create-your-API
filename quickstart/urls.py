from django.urls import path

from .views import ArticleGenericAPIView

urlpatterns = [
    path("article/<int:id>", ArticleGenericAPIView.as_view()),
    path("articles/", ArticleGenericAPIView.as_view()),
]
