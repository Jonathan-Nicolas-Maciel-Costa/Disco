from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm , AuthenticationForm

from .models import CustomUser
from django.contrib import messages


class CustomUserCreateForm(UserCreationForm):

    class Meta:
        model = CustomUser
        fields = ('username','matricula', 'first_name', 'last_name', 'phone', 'email', 'image')

        def save(self, commit=True):
            user: CustomUser = super().save(commit=False)
            user.set_password(self.cleaned_data["password1"])
            user.email = self.cleaned_data["email"]
            user.username = self.cleaned_data["username"]
            user.matricula = self.cleaned_data["matricula"]
            #user.username = user.email
            if commit:

                user.save()

            return user


class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = CustomUser
        fields = ('username', 'first_name', 'last_name', 'phone')
   
