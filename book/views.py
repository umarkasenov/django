from django.shortcuts import render
from . import models


def news_list(request):
    if request.method == 'GET':
        news = models.BlogNews.objects.all()
        return render(request, template_name='news.html',
                      context={'news': news})