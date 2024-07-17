from django.shortcuts import render, get_object_or_404
from django.views import View
from django.http import HttpResponse
from django.shortcuts import redirect
from django.urls import reverse
from .models import Article
from .forms import ArticleForm
from django.contrib import messages

class ArticleFormCreateView(View):

    def get(self, request, *args, **kwargs):
        form = ArticleForm()
        return render(request, 'articles/create.html', {'form': form})

    def post(self, request, *args, **kwargs):
        form = ArticleForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('articles')
        messages.error(request, 'Data is not valid.')
        return render(request, 'articles/create.html', context={'form': form})

class IndexView(View):

    def get(self, request, *args, **kwargs):
        articles = Article.objects.all()[:15]
        return render(request, 'articles/index.html', context={'articles': articles,})


class ArticleView(View):

    def get(self, request, *args, **kwargs):
        article = get_object_or_404(Article, id=kwargs['id'])
        return render(request, 'articles/show.html', context={'article': article,})


class ArticleFormEditView(View):

    def get(self, request, *args, **kwargs):
        article_id = kwargs.get('id')
        article = Article.objects.get(id=article_id)
        form = ArticleForm(instance=article)
        return render(request, 'articles/update.html', context={'form': form, 'article_id':article_id})

    def post(self, request, *args, **kwargs):
        article_id = kwargs.get('id')
        article = Article.objects.get(id=article_id)
        form = ArticleForm(request.POST, instance=article)
        if form.is_valid():
            messages.success(request, 'Article details updated.')
            form.save()
            return redirect('articles')
        messages.error(request, 'Incorrect data.')
        return render(request, 'articles/update.html', {'form': form, 'article_id':article_id})