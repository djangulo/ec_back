from django import forms

class HomeTextForm(forms.Form):
    home_text = forms.Textarea()