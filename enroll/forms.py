from dataclasses import field
from tkinter import Widget
from django import forms
from .models import User

class student(forms.ModelForm):
    class Meta:
        model=User
        fields =['name','email','password','repassword']
        Widget={
            'name':forms.TextInput(attrs={'class':'form-control'}),
            'email':forms.EmailInput(attrs={'class':'form-control'}),
            'password':forms.PasswordInput(attrs={'class':"form-control"}),
            'repassword':forms.PasswordInput(attrs={'class':"form-control"})
        }
    def clean(self):
      cleaned_data=super().clean()
      valpwd =cleaned_data['password']
      valrepwd = cleaned_data['repassword']
      if valpwd !=valrepwd:
        raise forms.ValidationError('password not match')