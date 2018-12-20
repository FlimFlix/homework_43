from django import forms
from webapp.models import Article, Comment


class ArticleCreateForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['user', 'title', 'text']


class ArticleUpdateForm(forms.ModelForm):
    class Meta:
        model = Article
        exclude = ['user']


class CommentCreateForm(forms.ModelForm):
    class Meta:
        model = Comment
        exclude = ['article']


class CommentUpdateForm(forms.ModelForm):
    class Meta:
        model = Comment
        exclude = ['user', 'article']


class ArticleSearchForm(forms.Form):
    article_name = forms.CharField(max_length=200, required=False, label='название_статьи')
