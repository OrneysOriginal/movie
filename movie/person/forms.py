from django import forms
import datetime


SIXTY_YEARS_IN_DAYS = 365 * 60
TEN_YEARS_IN_DAYS = 365 * 10


class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput())
    password = forms.CharField(widget=forms.PasswordInput())


class RegistrationForm(forms.Form):
    image = forms.ImageField()
    username = forms.CharField(widget=forms.TextInput())
    email = forms.EmailField(widget=forms.EmailInput())
    password = forms.CharField(widget=forms.PasswordInput())
    repeat_password = forms.CharField(widget=forms.PasswordInput())
    birthday = forms.DateField(
        required=False,
        widget=forms.DateInput(
            attrs={
                "type": "date",
                "min": datetime.date.today()
                - datetime.timedelta(days=SIXTY_YEARS_IN_DAYS),
                "max": datetime.date.today()
                - datetime.timedelta(days=TEN_YEARS_IN_DAYS),
                "class": "form-control",
            }
        ),
    )
