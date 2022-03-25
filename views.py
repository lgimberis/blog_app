from django.http import Http404
from django.shortcuts import render, get_object_or_404
from django.views.generic import ArchiveIndexView, ListView, DetailView

from .models import Article

ARTICLE_TEMPLATE_ROOT = "blog_app/content/"

class ArticleArchiveView(ArchiveIndexView):
    model = Article
    date_field = "published_datetime"
    context_object_name = "article_list"
    template_name = "blog_app/article_list.html"

def get_article(request, slug: str):
    article = get_object_or_404(Article, slug=slug)
    context = {
        "article": article,
    }
    return render(request, f"{ARTICLE_TEMPLATE_ROOT}{article.template_filename}", context=context)