from django.shortcuts import render
from django.views import View
from django.http import HttpResponse
from django.shortcuts import redirect
from django.urls import reverse

class MyView(View):

    def get(self, request, *args, **kwargs):
        return redirect(reverse('article', kwargs={'tags': 'python', 'article_id': 42}))


def index(request, tags, article_id):
    return HttpResponse(f'Статья номер {article_id}. Тег {tags}')