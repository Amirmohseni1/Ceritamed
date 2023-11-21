from django import forms
from phonenumber_field.widgets import PhoneNumberPrefixWidget

from .models import Consultation, ContactUs, Newsletters


class ContactUsModelForms(forms.ModelForm):
    class Meta:
        model = ContactUs
        fields = ('title', 'email', 'subject', 'body')
        widgets = {
            'title': forms.TextInput(attrs={"placeholder": "Your name", "class": "contact-control"}),
            'body': forms.Textarea(attrs={"placeholder": "Text", "class": "contact-control"}),
            'email': forms.EmailInput(attrs={"placeholder": "Email", "class": "contact-control"}),
            'subject': forms.TextInput(attrs={"placeholder": "Subject", "class": "contact-control"}),
        }


class ConsultationModelForm(forms.ModelForm):
    class Meta:
        model = Consultation
        fields = ('title', 'body', 'source', 'phone')
        widgets = {
            'title': forms.TextInput(attrs={"placeholder": "Your name"}),
            'body': forms.Textarea(attrs={"placeholder": "Text", "rows": "4"}),
            'phone': PhoneNumberPrefixWidget(attrs={"placeholder": "Your Number", "class": "contact-control"}),
            'source': forms.HiddenInput(),
        }
        labels = {
            'title': ('Your name'),
            'body': ('Text'),
            'phone': ('Whatsapp'),
        }


class NewsLettersForm(forms.ModelForm):
    class Meta:
        model = Newsletters
        fields = ('email',)
        widgets = {
            'email': forms.EmailInput(attrs={"placeholder": "Pleas write your EMAIL", "class": "input-newsletter"})
        }
