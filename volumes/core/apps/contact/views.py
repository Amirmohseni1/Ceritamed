from django.shortcuts import render
from django.contrib import messages
from apps.forms.models import ContactUsForm
from apps.forms.forms import ContactUsForms


# --------------------------------------------------- contact Page --------------------------------------------------------


def contact(request):
    contact_us_form: ContactUsForms = ContactUsForms(request.POST or None)
    if contact_us_form.is_valid():
        contact_us_form.save()
        messages.success(request, 'لقد تم إرسال إستمارتک بعنوان {} بنجاح '.format(contact_us_form.cleaned_data.get('subject')))
        contact_us_form: ContactUsForms = ContactUsForms()

    context = {
        'contact_us_form': contact_us_form,
    }
    return render(request, "contact-us/Contact.html", context)
