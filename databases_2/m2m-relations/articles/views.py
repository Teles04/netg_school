from django.views.generic import ListView
from django.shortcuts import render

from articles.models import Article, Teg


def articles_list(request):
    template = 'articles/news.html'
    object_list = Article.objects.all()
    for a in object_list:
        b = a.Tegs.filter()
        print(b.values)
    context = {'object_list': object_list}

    # используйте этот параметр для упорядочивания результатов
    # https://docs.djangoproject.com/en/2.2/ref/models/querysets/#django.db.models.query.QuerySet.order_by
    ordering = '-published_at'

    return render(request, template, context)
