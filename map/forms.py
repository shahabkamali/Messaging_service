from django.forms import ModelForm
from .models import Map,Floor


class AddMapForm(ModelForm):
    class Meta:
        model = Map
        fields = ['mapname', 'floor', 'picture']

class EditMapForm(ModelForm):
    class Meta:
        model = Map
        fields = ['mapname', 'picture']


class AddFloorForm(ModelForm):
    class Meta:
        model = Floor
        fields = ['name', 'building']