from django import forms
from .models import *
from django.core.exceptions import ValidationError



class ContactUsForm(forms.ModelForm):
    class Meta:
        model = ContactUsModel
        fields = '__all__'

        def clean_phone(self):
            phone = self.cleaned_data.get("phone")
            if not phone.isdigit() or len(phone) != 11:
                raise ValidationError("شماره تلفن باید ۱۱ رقم باشد.")
            return phone
