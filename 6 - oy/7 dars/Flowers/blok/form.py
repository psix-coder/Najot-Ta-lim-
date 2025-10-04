from django import forms
from blok.models import Turlar

class GullarForm(forms.Form):
    name = forms.CharField(max_length=100, widget=forms.TextInput(), label='Nomi')
    price = forms.IntegerField(widget=forms.Textarea(), label='Narxi')
    type = forms.ModelChoiceField(queryset=Turlar.objects.all(), widget=forms.Select(), label="Turi")