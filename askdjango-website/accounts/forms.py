from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.core.validators import validate_email
from .models import User, Profile
from django.contrib.auth.forms import AuthenticationForm
import unicodedata


class SignupForm(UserCreationForm):
    bio = forms.CharField(required=False)
    website_url = forms.URLField(required=False)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].validators = [validate_email]
        self.fields['username'].help_text = 'Enter Email Format.'
        self.fields['username'].label = 'Email'

    def save(self):
        user = super().save(commit=False)
        user.email = user.username
        user.save()

        bio = self.cleaned_data.get('bio', None)
        website_url = self.cleaned_data.get('website_url', None)

        Profile.objects.create(user=user, bio=bio, website_url=website_url)

        return user

    class Meta(UserCreationForm.Meta):
        model = User
        fields = UserCreationForm.Meta.fields + ('bio', 'website_url')


    '''
    def clean_username(self):
        value = self.cleaned_data.get('username')
        if value:
            validate_email(value)
        return value
    '''


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['bio', 'website_url']

class UsernameField(forms.CharField):
    def to_python(self, value):
        return unicodedata.normalize('NFKC', super().to_python(value))

class LoginForm(AuthenticationForm):
    username = UsernameField(
        label= 'Email',
        widget=forms.TextInput(attrs={'autofocus': True,  'class':'form-control', 'placeholder':'Your Email', 'requidred':True, 'style':'margin-top:20px; margin-bottom: 10px;'})
    )
    password = forms.CharField(
        label= "Password",
        strip=False,
        widget=forms.PasswordInput(attrs={'class':'form-control', 'id':'upw', 'placeholder':'Password', 'required': True}),
    )