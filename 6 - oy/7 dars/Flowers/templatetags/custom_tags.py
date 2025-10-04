from django import template
from blok.models import Turlar

register = template.Library()

@register.simple_tag
def get_all_turlar():
    return Turlar.objects.all()
