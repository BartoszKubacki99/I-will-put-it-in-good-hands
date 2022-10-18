import validators as validators
from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm

from .models import Donation, CustomUser


class AddDonationForm(ModelForm):
    class Meta:
        model = Donation
        fields = ('quantity', 'categories', 'institution', 'address',
                  'phone_number', 'city', 'zip_code', 'pick_up_date',
                  'pick_up_time', 'pick_up_comment')
        labels = {
            'quantity': '',
            'categories': '',
            'institution': '',
            'address': '',
            'phone_number': '',
            'city': '',
            'zip_code': '',
            'pick_up_date': '',
            'pick_up_time': '',
            'pick_up_comment': '',
            'user': '',
        }


class SignUpForm2(UserCreationForm):
    email = forms.EmailField(max_length=255, widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'email'}))
    first_name = forms.CharField(max_length=42, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Imię'}))
    last_name = forms.CharField(max_length=42, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nazwisko'}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Hasło'}))
    password2 = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Powtórz hasło'}))


    class Meta:
        model = CustomUser
        fields = ('first_name', 'last_name', 'email', 'password1', 'password2',)
        labels = {
            'first_name': '',
            'last_name': '',
            'email': '',
            'password1': '',
            'password2': '',

        }

