from django import forms
from django.contrib.auth.forms import UserCreationForm
from authentication.models import CustomUser  # სწორი User მოდელის იმპორტი

from users.models import Profile  # მხოლოდ იმ შემთხვევაში, თუ რეალურად იქ გიწერია ეს მოდელი

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'password1', 'password2']

class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = CustomUser
        fields = ['username', 'email']

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['bio', 'avatar']  # ეს ველები უნდა იყოს Profile მოდელში
