from django import forms


class ProductForm(forms.Form):
    code = forms.CharField(max_length=255)
    colour = forms.CharField(max_length=255)
    size = forms.IntegerField()
    gender = forms.