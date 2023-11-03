from django import forms


class ModelAddForm(forms.Form):
    one = forms.CharField(max_length=255, widget=forms.TextInput(attrs={'class':"form-control"}))
    two = forms.CharField(max_length=255, widget=forms.TextInput(attrs={'class':"form-control"}))
    three = forms.CharField(max_length=255, widget=forms.TextInput(attrs={'class':"form-control"}))

