"""
Forms for the webSite app
"""
from django import forms


class ConnexionForm(forms.Form):
    """
    Form for the connexion
    """
    username = forms.CharField(label="Nom d'utilisateur", max_length=30)
    password = forms.CharField(
        label="Mot de passe", widget=forms.PasswordInput)


class RegisterForm(forms.Form):
    """
    Form for the account registration
    """
    username = forms.CharField(label="Nom d'utilisateur", max_length=30)
    password = forms.CharField(
        label="Mot de passe", widget=forms.PasswordInput)
    email = forms.EmailField(label="Addresse mail", required=True)
