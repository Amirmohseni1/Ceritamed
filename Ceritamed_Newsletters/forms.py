from django import forms
from django.core import validators


class NewsLettersForm(forms.Form):
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={"placeholder": "يرجى إدخال بريدك الإلكتروني", "class": "input-newsletter"}),
    )
