from contact.forms import ConsultationModelForm
from django import template
from django.contrib import messages

register = template.Library()


@register.inclusion_tag('contact/consultation.html', takes_context=True)
def consultation_form(context):
    request = context['request']
    form = ConsultationModelForm(request.POST or None)
    if form.is_valid():
        commit_form = form.save(commit=False)
        commit_form.where = request.build_absolute_uri('?')
        commit_form.save()
        messages.success(request,
                         '{} لقد تم إرسال طلبک بنجاح و سیتواصل معک فریق سریتامد خلال الاربعة والعشرین ساعة القادمة '.format(
                             form.cleaned_data.get('full_name')))
        form = ConsultationModelForm()
    return {
        'form': form,
        'request': request
    }
