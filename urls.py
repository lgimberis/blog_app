from django.urls import path

from . import views

urlpatterns = [
    path("", views.ArticleArchiveView.as_view(), name="blog-app-index"),
    path("<str:slug>", views.get_article, name='blog-app-article'),
]