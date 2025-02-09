from django import forms
from .models import *



class SendOtpForm(forms.Form):
    phone = forms.CharField(max_length=11, label='شماره تلفن')


class UserLoginForm(forms.Form):
    phone = forms.CharField(max_length=300, label=' شماره تلفن', error_messages={'required': 'فیلد شماره تلفن نمی تواند خالی باشد', 'max_length': 'تلفن نامعتبر'})
    password = forms.CharField(max_length=25, label='پسورد', error_messages={'required': 'فیلد پسورد نمی تواند خالی باشد', 'max_length': 'پسورد نامعتبر'})


class UserRegisterForm(forms.Form):
    phone = forms.CharField(max_length=11, label='تلفن')

class UserRegisterActivationForm(UserRegisterForm):
    code = forms.CharField(max_length=6, label='کد')
    phone = forms.CharField(max_length=11, label='تلفن')
    fullname = forms.CharField(max_length=100, label='نام')
    password = forms.CharField(max_length=25, label='رمز عبور', widget=forms.PasswordInput)
    confirm_password = forms.CharField(max_length=25, label='تکرار رمز عبور', widget=forms.PasswordInput)

    def clean_password(self):
        password = self.cleaned_data.get('password')

        if not password:
            raise forms.ValidationError('رمز عبور الزامی است.')

        if password.isdigit() or password.isalpha() or password.lower() == password or len(password) < 8:
            raise forms.ValidationError('رمز عبور باید شامل اعداد و حروف بزرگ و کوچک باشد و حداقل ۸ کاراکتر باشد.')

        return password

    def clean_confirm_password(self):
        password = self.cleaned_data.get('password')
        confirm_password = self.cleaned_data.get('confirm_password')

        if confirm_password != password:
            raise forms.ValidationError('پسورد و تکرار آن یکسان نیستند.')

        return confirm_password

class ForgetForm(forms.Form):
    phone = forms.CharField(max_length=11, label='شماره تلفن')
    code = forms.CharField(max_length=6, label='کد')


class UserFileForm(forms.Form):
    file = forms.FileField(required=True)


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserModel
        fields = ['fullname', 'email', 'address', 'profile_image']



class ChangePasswordForm(forms.Form):
    old_password = forms.CharField(max_length=25, label='رمز عبور قدیمی')
    new_password = forms.CharField(max_length=25, label='رمز عبور جدید')
    confirm_password = forms.CharField(max_length=25, label='تکرار رمز عبور')

    def clean_confirm_password(self):
        confirm_password = self.cleaned_data['confirm_password']
        password = self.cleaned_data['new_password']

        if confirm_password == password:
            if password.isdigit() or password.isalpha() or password.lower() == password or len(password) < 8:
                raise forms.ValidationError('پسورد باید شامل اعداد و حروف کوچک و بزرگ باشد و حداقل 8 کاراکتر.')
            else:
                return confirm_password
        else:
            raise forms.ValidationError('پسورد و تکرار آن یکی نمی باشد')
