from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import  ValidationError
from .models import UserProfile


class UserAddForm(forms.Form):
        username = forms.CharField(label='UserName',
                                   widget=forms.TextInput(attrs={'placeholder': 'Username', 'class': 'form-control'}))
        firstname = forms.CharField(label='FirstName',
                                    widget=forms.TextInput(attrs={'placeholder': 'FirstName', 'class': 'form-control'}))
        lastname = forms.CharField(label='LastName',
                                   widget=forms.TextInput(attrs={'placeholder': 'LastName', 'class': 'form-control'}))
        email = forms.EmailField(widget=forms.TextInput(attrs={'placeholder': 'Email', 'class': 'form-control'}))
        password1 = forms.CharField(label='Password',
                                    widget=forms.PasswordInput(attrs={'placeholder':'Password', 'class': 'form-control'}))
        password2 = forms.CharField(label='Retype Password',
                                    widget=forms.PasswordInput(attrs={'placeholder':'RetypePassword', 'class': 'form-control'}))
        picture = forms.ImageField(required=False)

        def clean_username(self):
            data = self.cleaned_data['username']
            if User.objects.filter(username=data).exists():
                raise ValidationError('Username already taken.')
            return data

        def clean_email(self):
            data = self.cleaned_data['email']
            if User.objects.filter(email=data).exists():
                raise ValidationError('this email exists.')
            return data

        def clean_password2(self):
            password1 = self.cleaned_data.get('password1')
            password2 = self.cleaned_data.get('password2')

            if not password2:
                raise forms.ValidationError("You must confirm your password")
            if password1 != password2:
                raise forms.ValidationError("Your passwords do not match")
            return password2


class UserEditForm(forms.Form):
        id = forms.CharField(widget=forms.HiddenInput(), required=False, label='')
        firstname = forms.CharField(label='FirstName',
                                    widget=forms.TextInput(attrs={'placeholder': 'FirstName', 'class': 'form-control'}))
        lastname = forms.CharField(label='LastName',
                                   widget=forms.TextInput(attrs={'placeholder': 'LastName', 'class': 'form-control'}))
        email = forms.EmailField(widget=forms.TextInput(attrs={'placeholder': 'Email', 'class': 'form-control'}))
        picture = forms.ImageField(required=False)


class UserChagePassword(forms.Form):
    id = forms.CharField(widget=forms.HiddenInput(), required=False, label='')
    oldpassword = forms.CharField(label='Old Password',
                                    widget=forms.PasswordInput(attrs={'placeholder': 'Old Password', 'class': 'form-control'}))
    password1 = forms.CharField(label='New Password',
                                    widget=forms.PasswordInput(attrs={'placeholder': 'New Password', 'class': 'form-control'}))
    password2 = forms.CharField(label='Retype Password',
                                    widget=forms.PasswordInput(attrs={'placeholder':'RetypePassword', 'class': 'form-control'}))

    def clean_oldpassword(self):
        id = self.cleaned_data.get('id')
        oldpass = self.cleaned_data.get('oldpassword')
        user = User.objects.get(id=id)
        if not user.check_password(oldpass):
            raise forms.ValidationError("invalid old password")
        return oldpass

    def clean_password2(self):
            password1 = self.cleaned_data.get('password1')
            password2 = self.cleaned_data.get('password2')
            if not password2:
                raise forms.ValidationError("You must confirm your password")
            if password1 != password2:
                raise forms.ValidationError("Your passwords do not match")
            return password2