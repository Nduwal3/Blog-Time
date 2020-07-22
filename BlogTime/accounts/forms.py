from django import forms

# from django.contrib.auth.models import


class LoginForm(forms.Form):
    """Form definition for MODELNAME."""
    username = forms.CharField(max_length=150)
    password = forms.CharField(max_length=128, widget=forms.PasswordInput())

    # class Meta:
    #     """Meta definition for MODELNAMEform."""

    #     model = MODELNAME
    #     fields = ('',)
