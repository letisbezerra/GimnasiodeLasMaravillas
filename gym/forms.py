from django.forms import ModelForm
from django import forms 

class contactForm(forms.Form): 
    email = forms.EmailField()
    message = forms.CharField(widget=forms.Textarea)