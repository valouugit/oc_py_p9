from django import forms

class Follow(forms.Form):
    follow = forms.CharField(
        label="",
        max_length=20,
        widget=forms.TextInput(attrs={
            "placeholder": "Nom d'utilisateur",
            "class": "w-72 p-2 rounded-md focus-visible:border-10 border-2 border-green-800 hover:border-green-500"
        })
    )