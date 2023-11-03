from django import forms


class ModelAddForm(forms.Form):
    one = forms.CharField(max_length=255)
    two = forms.CharField(max_length=255)
    three = forms.CharField(max_length=255)

