from django import forms

class ReviewForms(forms.Form):
    user_name = forms.CharField()