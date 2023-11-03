from django import forms


class ModelAddForm(forms.Form):
    one = forms.CharField(max_length=255, widget=forms.TextInput(attrs={'class':"form-control p-1"}))
    two = forms.CharField(max_length=255, widget=forms.TextInput(attrs={'class':"form-control p-1"}))
    three = forms.CharField(max_length=255, widget=forms.TextInput(attrs={'class':"form-control p-1"}))

