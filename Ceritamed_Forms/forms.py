from django import forms
from django.core import validators
from phonenumber_field.formfields import PhoneNumberField
from phonenumber_field.widgets import PhoneNumberPrefixWidget, PhonePrefixSelect, PhoneNumberInternationalFallbackWidget
from Ceritamed_Forms.models import Form, ContactUsForm


class ContactUsForms(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field in self.Meta.required:
            self.fields[field].required = True

    class Meta:
        model = ContactUsForm
        fields = ('full_name', 'email', 'subject', 'text')
        required = ('full_name', 'email', 'subject', 'text')
        widgets = {
            'full_name': forms.TextInput(attrs={"placeholder": "يرجى إدخال إسمك", "class": "form-control"}),
            'text': forms.Textarea(attrs={"placeholder": "يرجى إدخال الوصف الخاص بك", "class": "form-control"}),
            'email': forms.EmailInput(attrs={"placeholder": "يرجى إدخال بريدك الإلكتروني", "class": "form-control"}),
            'subject': forms.TextInput(attrs={"placeholder": "الرجاء إدخال موضوعك", "class": "form-control"}),
        }


class Form1(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field in self.Meta.required:
            self.fields[field].required = True

    class Meta:
        model = Form
        fields = ('full_name', 'text', 'where', 'phone')
        required = ('full_name', 'text', 'phone',)
        widgets = {
            'full_name': forms.TextInput(attrs={"placeholder": "يرجى إدخال إسمك"}),
            'text': forms.Textarea(attrs={"placeholder": "يرجى إدخال الوصف الخاص بك", "rows": "4"}),
            'phone': PhoneNumberPrefixWidget(attrs={"placeholder": "يرجى إدخال رقمك", "class": "form-control"}),
            'where': forms.HiddenInput(),
        }
        labels = {
            'full_name': ('إسمك'),
            'text': ('رسالتك'),
            'phone': ('Whatsapp'),
        }


class Form2(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field in self.Meta.required:
            self.fields[field].required = True

    class Meta:
        model = Form
        fields = ('full_name', 'text', 'where', 'phone', 'email')
        required = ('full_name', 'text', 'phone', 'email')
        widgets = {
            'full_name': forms.TextInput(attrs={"placeholder": "يرجى إدخال إسمك"}),
            'text': forms.Textarea(attrs={"placeholder": "يرجى إدخال الوصف الخاص بك", "rows": "4"}),
            'phone': PhoneNumberPrefixWidget(attrs={"placeholder": "يرجى إدخال رقمك", "class": "form-control"}),
            'email': forms.EmailInput(attrs={"placeholder": "يرجى إدخال بريدك الإلكتروني", "class": "form-control"}),
            'where': forms.HiddenInput(),
        }
        labels = {
            'full_name': ('إسمك'),
            'text': ('رسالتك'),
            'phone': ('Whatsapp'),
            'email': ('البريد الألكتروني'),
        }
