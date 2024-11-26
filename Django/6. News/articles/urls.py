from django.urls import path
from .views import (
   ArticleListView,
   ArticleDetailView,
   UpdateArticleView,
   DeleteArticleView,
   ArticleCreateView,
)



urlpatterns = [
  path("<int:pk>/", ArticleDetailView.as_view(),
 name="article_detail"), 
 path("<int:pk>/edit/", UpdateArticleView.as_view(),
 name="article_edit"), 
 path("<int:pk>/delete/", DeleteArticleView.as_view(),
 name="article_delete"), 
 path("articles/", ArticleListView.as_view(),
 name="article_list"),
 path("new/", ArticleCreateView.as_view(), 
 name="article_new"), 
      
]