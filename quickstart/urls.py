from django.urls import path

from .views import ArticleDeatils, ArticleAPIView

urlpatterns = [
    path("article/<int:id>", ArticleDeatils.as_view()),
    path("articles/", ArticleAPIView.as_view())
]
