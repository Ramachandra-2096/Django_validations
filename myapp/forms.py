from django import forms
from django.core import validators

#password validation
def pass_w(value):
    if len(value)<6:
        raise forms.ValidationError("The Re-Password is too short")
    
    
    
class StudentReg(forms.Form):
    name = forms.CharField(label= "Enter your name",max_length=50)
    email = forms.EmailField(label=" Enter your email",max_length=100)
    #3rd type of validation
    password = forms.CharField(widget=forms.PasswordInput,label="Enter password",validators=[validators.MinLengthValidator(6)])  
    re_pass= forms.CharField(widget=forms.PasswordInput,label="Enter Re_password",validators=[pass_w])
    # this is the second method
    def clean_name(self):
        name = self.cleaned_data.get('name')
        if len(name)<3:
            raise forms.ValidationError("Name is too shoart")
        return name