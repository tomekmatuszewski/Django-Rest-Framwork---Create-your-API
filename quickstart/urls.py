from django.urls import path

from .views import article_detail, article_list

urlpatterns = [
    path("articles/", article_list),
    path("article/<int:pk>", article_detail),
]
