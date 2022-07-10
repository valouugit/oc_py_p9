from django import forms

from lit.models import Ticket

class TicketAdd(forms.Form):
    title = forms.CharField(
        label="Titre",
        max_length=128,
        widget=forms.TextInput(attrs={
            "class": "p-2 rounded-md focus-visible:border-10 border-2 border-green-800 hover:border-green-500",
        }),
        required=True
    )
    description = forms.CharField(
        label="Description",
        max_length=2048,
        widget=forms.Textarea(attrs={
            "class": "p-2 rounded-md focus-visible:border-10 border-2 border-green-800 hover:border-green-500"
        }),
        required=True
    )
    image = forms.ImageField(
        required=True,
        widget=forms.FileInput(attrs={
            "class": "p-2 rounded-md focus-visible:border-10 border-2 border-green-800 hover:border-green-500"
        })
    )

    def save(self, request):
        cleaned = self.cleaned_data

        ticket = Ticket(
            title = cleaned["title"],
            description = cleaned["description"],
            user = request.user,
            image = cleaned["image"]
        )
        ticket.save()