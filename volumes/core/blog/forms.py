from django import forms
from blog.models import PostComment


class BlogComment(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(), required=True)
    email = forms.CharField(widget=forms.EmailInput(), required=True)
    text = forms.CharField(widget=forms.Textarea(), required=True)

    class Meta:
        model = PostComment
        fields = ('name', 'email', 'text')
