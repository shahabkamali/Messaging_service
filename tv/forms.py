from django import forms
from django.forms import ModelForm, Textarea

from models import Message

class AddMessageForm(ModelForm):
    class Meta:
        model = Message
        fields = ['name','showtime','context']
        widgets = {
            'text': Textarea(attrs={'cols': 80, 'rows': 40}),
        }

