from django import forms
from django.forms import ModelForm
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import ReadOnlyPasswordHashField


from .models import User

# from django.contrib.auth.models import
USER = get_user_model()


class UserModelForm(ModelForm):
    password1 = forms.CharField(
        label='Password', widget=forms.PasswordInput
    )
    password2 = forms.CharField(
        label='Confirm password', widget=forms.PasswordInput
    )
    class Meta:
        model = User
        fields = ['first_name', 'last_name','username','email', 'bio', 'dob', 'profile_img']

    def clean_password2(self):
        # Check that the two password entries match
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords do not match")
        return password2

    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user

class UserUpdateModelForm(ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name','username','email', 'bio', 'dob', 'profile_img']

    def clean_password(self):
# Password can't be changed in the admin
        return self.initial["password"]


class LoginForm(forms.Form):
    """Form definition for MODELNAME."""
    username = forms.CharField(max_length=150)
    password = forms.CharField(max_length=128, widget=forms.PasswordInput())

    # class Meta:
    #     """Meta definition for MODELNAMEform."""

    #     model = MODELNAME
    #     fields = ('',)

class RegisterForm(forms.Form):
    first_name = forms.CharField(max_length=30)
    last_name = forms.CharField(max_length=150)
    username = forms.CharField(max_length=150)
    email = forms.EmailField(max_length=150)
    password = forms.CharField(max_length=200, widget=forms.PasswordInput())
    confirm_password = forms.CharField(max_length=200, widget=forms.PasswordInput())

    def clean_username(self):
        if User.objects.filter(username=self.cleaned_data['username']).exists():
            raise forms.ValidationError("This Username is taken")
        return self.cleaned_data['username']
    
    def clean(self):
        password = self.cleaned_data['password']
        confirm_password = self.cleaned_data['confirm_password']
        if password != confirm_password:
            raise forms.ValidationError("passwords do not match")
