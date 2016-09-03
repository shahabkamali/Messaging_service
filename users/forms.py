from django import forms


class UserAddForm(forms.Form):
        username = forms.CharField(label='UserName', widget=forms.TextInput(attrs={'placeholder': 'Username'}))
        firstname = forms.CharField(label='FirstName', widget=forms.TextInput(attrs={'placeholder': 'FirstName'}))
        lastname = forms.CharField(label='LastName', max_length=100)
        email = forms.EmailField()
        password1 = forms.CharField(widget=forms.PasswordInput)
        password2 = forms.CharField(widget=forms.PasswordInput)

        def clean_username(self):
            data = self.cleaned_data['username']
            if User.objects.filter(username=data).exists():
                raise ValidationError('Username already taken.')
            return data

        def clean(self):
            password1 = self.cleaned_data.get('password1')
            password2 = self.cleaned_data.get('password2')

            if password1 and password1 != password2:
                raise forms.ValidationError("Passwords don't match")

            return self.cleaned_data
