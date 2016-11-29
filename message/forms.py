from django import forms
from django.forms import ModelForm,Textarea

from models import Message

class AddMessageForm(ModelForm):
    class Meta:
        model = Message
        fields = ['text', 'x', 'y', 'r', 'g', 'b', 'brightness', 'effect', 'showtime','font']
        widgets = {
            'text': Textarea(attrs={'cols': 80, 'rows': 5}),
        }

