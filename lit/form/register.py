from typing import Any
from django.contrib.auth.forms import UserCreationForm

class RegisterForm(UserCreationForm):

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)
        for visible_field in self.visible_fields():
            visible_field.field.widget.attrs['class'] = "w-72 p-2 rounded-md focus-visible:border-10 border-2 border-green-800 hover:border-green-500"