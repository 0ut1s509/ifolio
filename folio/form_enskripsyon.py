from django import forms
from django.contrib.auth.models import User


class EnkripsyonForm(forms.ModelForm):
    class Meta:
        model=User
        fields=('username', "password")
        widgets={
            "username":forms.TextInput(),
            "password":forms.PasswordInput(),
        }
   
    def clean(self):
        cleaned_data = super().clean()

        email=cleaned_data.get('username')
        modpas=cleaned_data.get('password')

  


