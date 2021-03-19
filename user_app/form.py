from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User
from django.forms import ValidationError


class SignUpForm(UserCreationForm):
    username = forms.CharField(max_length=20, required=True, label="username", widget=forms.TextInput(
        attrs={'placeholder': 'Write Your username', }))
    email = forms.EmailField(max_length=50, label='email', required=True, widget=forms.EmailInput(
        attrs={'placeholder': 'Write Your email'}))
    first_name = forms.CharField(max_length=80, label="first_name", required=True, widget=forms.TextInput(
        attrs={'placeholder': 'Write Your first name'}))
    last_name = forms.CharField(max_length=40, label="last_name", required=True, widget=forms.TextInput(
        attrs={'placeholder': 'Write Your last name'}))

    class Meta:
        model = User
        fields = ['username', 'email', 'first_name',
                  'last_name', 'password1', 'password2']
        widgets = {
            'password1': forms.PasswordInput(attrs={'placeholder': 'Enter New Password',
                                                    'class': 'form-control'}),
            'password2': forms.PasswordInput(attrs={'placeholder': 'Enter Repeat password',
                                                    'class': 'form-control'}),
        }

    def clean_email(self):
        email = self.cleaned_data['email']
        user = None
        try:
            user = User.objects.get(email=email)
        except:
            return email
        if (user is not  None):
            raise ValidationError("User Email Already Exists");
