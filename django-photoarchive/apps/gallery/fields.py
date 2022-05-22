from django import forms
from .models import Tag
from django.forms import formset_factory


class TagForm(forms.Form):
    name = forms.CharField()

class PeopleForm(forms.Form):
    name = forms.CharField()

class FilterForm(forms.Form):
    author = forms.CharField(
        required=False
    )

    start_year = forms.IntegerField(
        min_value=1900,
        max_value=2200,
        required=False
    )

    end_year = forms.IntegerField(
        min_value=1900,
        max_value=2200, 
        required=False
    )