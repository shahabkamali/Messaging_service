from django import forms
from django.forms import ModelForm

from models import Voice

class AddVoiceForm(ModelForm):
    class Meta:
        model = Voice
        fields = ['name', 'filename']


