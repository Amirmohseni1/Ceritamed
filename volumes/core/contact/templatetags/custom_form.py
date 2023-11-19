from contact.forms import Form1, Form2
from django import template
from django.contrib import messages

register = template.Library()


@register.inclusion_tag('form/form_1.html', takes_context=True)
def form1(context):
    request = context['request']
    form: Form1 = Form1(request.POST or None)
    if form.is_valid():
        commit_form = form.save(commit=False)
        commit_form.where = request.build_absolute_uri('?')
        commit_form.save()
        messages.success(request,
                         '{} لقد تم إرسال طلبک بنجاح و سیتواصل معک فریق سریتامد خلال الاربعة والعشرین ساعة القادمة '.format(
                             form.cleaned_data.get('full_name')))
        form: Form1 = Form1()
    return {
        'form': form,
        'request': request
    }


@register.inclusion_tag('form/form_2.html', takes_context=True)
def form2(context):
    request = context['request']
    form: Form2 = Form2(request.POST or None)
    if form.is_valid():
        commit_form = form.save(commit=False)
        commit_form.where = request.build_absolute_uri('?')
        commit_form.save()
        messages.success(request,
                         '{} لقد تم إرسال طلبک بنجاح و سیتواصل معک فریق سریتامد خلال الاربعة والعشرین ساعة القادمة '.format(
                             form.cleaned_data.get('full_name')))
        form: Form2 = Form2()
    return {
        'form': form,
        'request': request
    }
