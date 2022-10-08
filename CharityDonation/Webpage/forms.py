from django import forms
from django.forms import ModelForm

from .models import Donation


class AddDonationForm(ModelForm):
    class Meta:
        model = Donation
        fields = '__all__'
        labels = {
            'quantity': '',
            'categories': '',
            'institution': '',
            'address': '',
            'phone_number': '',
            'city': '',
        }