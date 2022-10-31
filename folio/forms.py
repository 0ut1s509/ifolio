from django import forms
from .models import *
from django.contrib.auth.models import User

chwa = (('design', 'DESIGN'), ('food','FOOD'), ('education','EDUCATION'), ('energy','ENERGY'), ('technology','TECHNOLOGIE'), ('programming','PROGRAMMING'), ('health',' HEALTH'), ('finance','FINANCE'), ('money','MONEY'))


class NewProjectForm(forms.ModelForm):
   
    class Meta:
        model=Project
        fields = ('tit','deskripsyon', 'foto', 'categorys') 


        widgets ={
                'tit' : forms.TextInput(attrs={'class':'form-control'}),
                'deskripsyon':forms.TextInput(attrs={'class':'form-control'}),
                'foto' : forms.FileInput(attrs={'class':'form-control'}),
                'categorys' : forms.SelectMultiple(choices=chwa, attrs={'class':'form-control'}),
        }

    def clean(self):
        cleaned_data=super().clean()
      
class UpdateProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('foto', 'non', 'siyati','imel', 'telefon')
        widgets = {
            'foto' : forms.FileInput(attrs={'class': 'form-control'}),
            'non'  : forms.TextInput(attrs={'class': 'form-control', 'placeholder':"Enter your first name"}),
            'siyati' : forms.TextInput(attrs={'class': 'form-control', 'placeholder':"Enter your last name"}),
            'imel' : forms.EmailInput(attrs={'class': 'form-control', 'placeholder':"Enter your Email"}),
            'telefon' : forms.TextInput(attrs={'class': 'form-control', 'placeholder':"Enter your phone number"}),
        }

    