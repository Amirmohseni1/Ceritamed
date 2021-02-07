from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags


class EmailService:

    @staticmethod
    def send_email(subject, context, template_address, to):
        try:
            html_message = render_to_string(template_address, context)
            plain_message = strip_tags(html_message)
            from_email = 'mail.ceritamed.com'
            send_mail(subject, plain_message, from_email, [to], html_message=html_message)
        except:
            pass
