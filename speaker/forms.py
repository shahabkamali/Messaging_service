from django import forms
from django.forms import ModelForm

from models import Voice

class AddVoiceForm(ModelForm):
    class Meta:
        model = Voice
        fields = ['name', 'filename']
    # def clean_filename(self):
    #     filename = self.cleaned_data.get(['photo'])
    #
    #
    #
    #     def clean_photo(self):
    #         photo = self.cleaned_data.get(['photo'])
    #         if photo:
    #             format = Image.open(photo.file).format
    #             photo.file.seek(0)
    #             if format in settings.VALID_IMAGE_FILETYPES:
    #                 return photo
    #         raise forms.ValidationError(...)

