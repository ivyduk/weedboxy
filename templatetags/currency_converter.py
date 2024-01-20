from django import template
from django.contrib.humanize.templatetags.humanize import intcomma


register = template.Library()

@register.filter(name='currency')
def currency(dollars):
    dollars = round(int(dollars), 0)  
    return "$%s" % intcomma(dollars)  
