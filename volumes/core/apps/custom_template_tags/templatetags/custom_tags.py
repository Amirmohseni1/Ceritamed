from django import template
from utils.jalali.JalaliServices import jalali_converter_day, jalali_converter_months, jalali_converter_day_and_month, \
    jalali_converter_date
from django.db.models import Count

register = template.Library()


# ------------------------------------------------------------ jalali tags ------------------------------------------------------

@register.filter()
def jalali_day(date):
    return jalali_converter_day(date)


@register.filter()
def jalali_months(date):
    return jalali_converter_months(date)


@register.filter()
def jalali_date(date):
    return jalali_converter_date(date)


@register.filter()
def jalali_day_and_month(date):
    return jalali_converter_day_and_month(date)


# ------------------------------------------------------------ Pagination tags ------------------------------------------------------

@register.simple_tag
def URL(value, name, urlencode=None):
    url = '?{}={}'.format(name, value)

    if urlencode:
        querystring = urlencode.split('&')
        filtered_querystring = filter(lambda p: p.split('=')[0] != name, querystring)
        encoded_querystring = '&'.join(filtered_querystring)
        url = '{}&{}'.format(url, encoded_querystring)

    return url
