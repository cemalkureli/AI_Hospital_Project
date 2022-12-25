from django import forms 
from django.contrib.auth.models import User

class RegisterForm(forms.Form):

    username =  forms.CharField(max_length=20, required=True, label= "Username", widget=forms.TextInput(attrs={'placeholder': 'Username'})) 
    password = forms.CharField(max_length=20, required=True, label= "Password", widget=forms.PasswordInput(attrs={'placeholder': 'Password'}))  
    confirm_password =  forms.CharField(max_length=20, required=True, label= "Password(Again)", widget=forms.PasswordInput(attrs={'placeholder': 'Password(Again)'}))
    first_name = forms.CharField(max_length = 20, required=True, label='First Name',widget=forms.TextInput(attrs={'placeholder': 'Name'}))
    last_name = forms.CharField(max_length = 20, required=True, label='Last Name',widget=forms.TextInput(attrs={'placeholder': 'Surname'}))
    email =  forms.EmailField(max_length = 50, required=True, label='E-mail',widget=forms.TextInput(attrs={'placeholder': 'E-mail'}))
    
    
    def clean(self) -> dict[str]:  
        
        username = self.cleaned_data.get("username")
        password = self.cleaned_data.get("password")
        confirm = self.cleaned_data.get("confirm_password")
        name = self.cleaned_data.get("first_name")
        surname = self.cleaned_data.get("last_name")
        email = self.cleaned_data.get("email")
                
        if User.objects.filter(username__iexact=username).exists():
            raise forms.ValidationError('The entered username has been used before. Please enter another username.')

        if password and confirm and password != confirm:
            raise forms.ValidationError("Passwords do not match.")

        value = {
            "username" : username,
            "password" : password,
            "name" : name,
            "surname" : surname,
            "email" : email,
        }

        return value

class LoginForm(forms.Form):
    username = forms.CharField(max_length=20, required=False, label = "Username", widget=forms.TextInput(attrs={'placeholder': 'Username'}))
    password = forms.CharField(max_length=20, required=False, label = "Password", widget=forms.PasswordInput(attrs={'placeholder': 'Password'}))
