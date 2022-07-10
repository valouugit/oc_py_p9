from django import forms

class Unfollow(forms.Form):
    unfollow = forms.CharField(
        label="",
        max_length=20,
        widget=forms.HiddenInput()
    )