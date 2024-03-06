from django import forms

from newspaper.models import Newspaper


class NewspaperForm(forms.ModelForm):
    class Meta:
        model = Newspaper
        fields = '__all__'
