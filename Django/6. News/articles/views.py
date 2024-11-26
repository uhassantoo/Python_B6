from django.shortcuts import render
from django.views.generic import ListView,DetailView
from django.views.generic.edit import UpdateView, DeleteView , CreateView
from .models import Article
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.
class ArticleListView(ListView):
    model = Article
    template_name = 'article_list.html'
    
class ArticleDetailView(DetailView):
    model = Article
    template_name = 'article_detail.html'
    
class UpdateArticleView(UpdateView):
    model = Article
    fields = (
        'title',
        'body',
    )
    template_name = 'article_edit.html'

class DeleteArticleView(DeleteView):
    model = Article
    template_name = 'article_delete.html'
    success_url = reverse_lazy('article_list')
    

class ArticleCreateView(CreateView , LoginRequiredMixin): 
    model = Article
    template_name = "article_new.html"
    fields = (
                "title",
                "body",
               
             )
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    success_url = '/articles/' 
