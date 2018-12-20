from django.views.generic import ListView, DetailView, CreateView, UpdateView, TemplateView, View, RedirectView, \
    FormView
from webapp.models import User, Article, Comment, Rating
from django.urls import reverse_lazy, reverse
from webapp.forms import ArticleCreateForm, ArticleUpdateForm, CommentCreateForm, CommentUpdateForm, ArticleSearchForm
from django.shortcuts import get_object_or_404


class ArticleListView(ListView, FormView):
    model = Article
    template_name = 'article_list.html'
    form_class = ArticleSearchForm

    def get_queryset(self):
        article_name = self.request.GET.get('article_name')
        if article_name:
            return Article.objects.filter(title__icontains=article_name)
        else:
            return Article.objects.all()


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


class CommentCreateView(CreateView):
    model = Comment
    form_class = CommentCreateForm
    template_name = 'comment_create.html'

    def get_success_url(self):
        return reverse('article_detail', kwargs={'pk': self.kwargs['pk']})

    def form_valid(self, form):
        form.instance.article = get_object_or_404(Article, pk=self.kwargs['pk'])
        return super().form_valid(form)


class CommentUpdateView(UpdateView):
    model = Comment
    form_class = CommentUpdateForm
    template_name = 'comment_update.html'

    def get_success_url(self):
        return reverse('article_detail', kwargs={'pk': self.kwargs['pk']})