from django import forms
from .models import Tag
from django.forms import formset_factory


class TagForm(forms.Form):
    tag_name = forms.CharField()

    def add_fields(self, form, index):
        super().add_fields(form, index)
        form.fields["tag_field"] = forms.CharField()

class PeopleForm(forms.Form):
    person_name = forms.CharField()

    def add_fields(self, form, index):
        super().add_fields(form, index)
        form.fields["person_field"] = forms.CharField()

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

    tag_formset = formset_factory(TagForm, max_num=5, absolute_max=5, validate_max=True, extra=5)
    people_formset = formset_factory(PeopleForm, max_num=5, absolute_max=5, validate_max=True, extra=5)