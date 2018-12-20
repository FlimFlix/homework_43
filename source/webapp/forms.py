from django import forms
from webapp.models import Article


class ArticleCreateForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['user', 'title', 'text']


class ArticleUpdateForm(forms.ModelForm):
    class Meta:
        model = Article
        exclude = ['user']


