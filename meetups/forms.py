from django import forms
from .models import Participant

#class RegistrationForm(forms.ModelForm): # has automatic save method
#  class Meta:
#      model = Participant
#      fields = ['email'] # which fields to show on form

class RegistrationForm(forms.Form):
    email = forms.EmailField(label='Your Email')