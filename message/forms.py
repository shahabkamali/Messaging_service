from django import forms

class AddMessageForm(ModelForm):
    class Meta:
        model = Map
        fields = ['text', 'x', 'y', 'r', 'g', 'b', 'brightness', 'effect', 'showtime']