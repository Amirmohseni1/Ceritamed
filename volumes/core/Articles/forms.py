from django import forms

from .models import ArticleComment


class ArticleCommentModelForm(forms.ModelForm):
    class Meta:
        model = ArticleComment
        fields = ('name', 'email', 'body')
