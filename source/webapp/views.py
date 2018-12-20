from django.views.generic import ListView, DetailView, CreateView, UpdateView, TemplateView, View, RedirectView
from webapp.models import User, Article, Comment, Rating
from django.urls import reverse_lazy
from webapp.forms import ArticleCreateForm, ArticleUpdateForm


class ArticleListView(ListView):
    model = Article
    template_name = 'article_list.html'


class ArticleDetailView(DetailView):
    model = Article
    template_name = 'article_detail.html'


class UserListView(ListView):
    model = User
    template_name = 'user_list.html'


class UserDetailView(DetailView):
    model = User
    template_name = 'user_detail.html'


class ArticleCreateView(CreateView):
    model = Article
    form_class = ArticleCreateForm
    template_name = 'article_create.html'
    success_url = reverse_lazy('article_list')


class ArticleUpdateView(UpdateView):
    model = Article
    form_class = ArticleUpdateForm
    template_name = 'article_update.html'
    success_url = reverse_lazy('article_list')






