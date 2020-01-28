from django import forms

class UserLoginForm(forms.Form):
    """
    Form to log user in
    """
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)