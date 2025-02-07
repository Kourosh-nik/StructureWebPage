from django import forms
from .models import *
from django.core.validators import MinLengthValidator


class SendOtpForm(forms.Form):
    phone = forms.CharField(max_length=11, label='شماره تلفن')


class UserLoginForm(forms.Form):
    phone = forms.CharField(max_length=300, label=' شماره تلفن', error_messages={'required': 'فیلد شماره تلفن نمی تواند خالی باشد', 'max_length': 'تلفن نامعتبر'})
    password = forms.CharField(max_length=25, label='پسورد', error_messages={'required': 'فیلد پسورد نمی تواند خالی باشد', 'max_length': 'پسورد نامعتبر'})


class UserRegisterForm(forms.Form):
    phone = forms.CharField(max_length=11, label='تلفن')
    fullname = forms.CharField(max_length=1000, label='نام')
    password = forms.CharField(max_length=25, label='رمز عبور')
    confirm_password = forms.CharField(max_length=25, label='تکرار رمز عبور')

    def clean_confirm_password(self):
        confirm_password = self.cleaned_data['confirm_password']
        password = self.cleaned_data['password']

        if confirm_password == password:
            if password.isdigit() or password.isalpha() or password.lower() == password or len(password) < 8:
                raise forms.ValidationError('پسورد باید شامل اعداد و حروف کوچک و بزرگ باشد و حداقل 8 کاراکتر.')
            else:
                return confirm_password
        else:
            raise forms.ValidationError('پسورد و تکرار آن یکی نمی باشد')


class UserRegisterActivationForm(forms.Form):
    code = forms.CharField(max_length=6, label='کد')
    phone = forms.CharField(max_length=11, label='شماره تلفن')
    fullname = forms.CharField(max_length=1000, label='نام')
    password = forms.CharField(max_length=25, label='رمز عبور')
    confirm_password = forms.CharField(max_length=25, label='تکرار رمز عبور')

    def clean_confirm_password(self):
        confirm_password = self.cleaned_data['confirm_password']
        password = self.cleaned_data['password']

        if confirm_password == password:
            if password.isdigit() or password.isalpha() or password.lower() == password or len(password) < 8:
                raise forms.ValidationError('پسورد باید شامل اعداد و حروف کوچک و بزرگ باشد و حداقل 8 کاراکتر.')
            else:
                return confirm_password
        else:
            raise forms.ValidationError('پسورد و تکرار آن یکی نمی باشد')


class ForgetForm(forms.Form):
    phone = forms.CharField(max_length=11, label='شماره تلفن')
    code = forms.CharField(max_length=6, label='کد')


class UserFileForm(forms.Form):
    file = forms.FileField(required=True)
