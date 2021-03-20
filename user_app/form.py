from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User
from django.forms import ValidationError


class SignUpForm(UserCreationForm):
    username = forms.CharField(max_length=20, required=True, label="username", widget=forms.TextInput(
        attrs={'placeholder': 'Write Your username', 'class': 'form-control'}))
    email = forms.EmailField(max_length=50, required=True)
    first_name = forms.CharField(max_length=80, label="first_name", required=True, widget=forms.TextInput(
        attrs={'placeholder': 'Write Your first name', 'class': 'form-control'}))
    last_name = forms.CharField(max_length=40, label="last_name", required=True, widget=forms.TextInput(
        attrs={'placeholder': 'Write Your last name', 'class': 'form-control'}))

    # password1 = forms.CharField(max_length=20, required=True, label="password", widget=forms.TextInput(
    #     attrs={'placeholder': 'Write Your password', 'class': 'form-control'}))
    # password2 = forms.CharField(max_length=20, required=True, label="password", widget=forms.TextInput(
    #     attrs={'placeholder': 'Write Your Conform password', 'class': 'form-control'}))

    class Meta:
        model = User
        fields = ['username', 'first_name',
                  'last_name', 'email', 'password1', 'password2']
        # widgets = {
        #     'password1': forms.PasswordInput(attrs={'placeholder': 'Enter New Password',
        #                                             'class': 'form-control'}),
        #     'password2': forms.PasswordInput(attrs={'placeholder': 'Enter Repeat password',
        #                                             'class': 'form-control'}),

    def clean_email(self):
        email = self.cleaned_data['email']
        user = None
        try:
            user = User.objects.get(email=email)
        except:
            return email
        if user is not None:
            raise ValidationError("User Email Already Exists");
