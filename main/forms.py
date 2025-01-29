from django import forms
from .models import *


class TalabaForm(forms.Form):
    ism = forms.CharField(max_length=50)
    guruh = forms.CharField(max_length=20)
    kurs = forms.IntegerField(min_value=1, max_value=4)
    kitob_soni = forms.IntegerField(min_value=0)


class KitobForm(forms.ModelForm):
    class Meta:
        model = Kitob
        fields = '__all__'
