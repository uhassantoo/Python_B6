from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.edit import UpdateView, DeleteView, CreateView, FormView
from .models import Article
from django.views.generic.detail import SingleObjectMixin
from django.urls import reverse_lazy, reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import CommentForm
# Create your views here.


class ArticleListView(ListView):
    model = Article
    template_name = 'article_list.html'


class CommentGet(DetailView):
    model = Article
    template_name = 'article_detail.html'


class CommentPost(SingleObjectMixin, FormView):  # new
    model = Article
    form_class = CommentForm
    template_name = "article_detail.html"

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super().post(request, *args, **kwargs)

    def form_valid(self, form):
        comment = form.save(commit=False)
        comment.article = self.object
        comment.author = self.request.user
        comment.save()
        return super().form_valid(form)

    def get_success_url(self):
        article = self.object
        return reverse("article_detail", kwargs={"pk": article.pk})

class ArticleDetailView(LoginRequiredMixin, DetailView):
    def get(self, request, *args, **kwargs):
        view=CommentGet.as_view()
        return view(request, *args, **kwargs)


    def post(self, request, *args, **kwargs):
        view=CommentPost.as_view()
        return view(request, *args, **kwargs)


class UpdateArticleView(UpdateView):
    model=Article
    fields=(
        'title',
        'body',
    )
    template_name='article_edit.html'

class DeleteArticleView(DeleteView):
    model=Article
    template_name='article_delete.html'
    success_url=reverse_lazy('article_list')


class ArticleCreateView(CreateView, LoginRequiredMixin):
    model=Article
    template_name="article_new.html"
    fields=(
                "title",
                "body",

             )
    def form_valid(self, form):
        form.instance.author=self.request.user
        return super().form_valid(form)
    success_url='/articles/'
