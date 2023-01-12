from django import forms 
from django.contrib.auth.models import User
from user.models import RegisterDoctor,DoctorLogin
from phonenumber_field.formfields import PhoneNumberField

class RegisterForm(forms.Form):

    username =  forms.CharField(max_length=20, required=True, label= "Kullanıcı Adı", widget=forms.TextInput(attrs={'placeholder': 'Kullanıcı Adı','style':"text-align: center;"})) 
    password = forms.CharField(max_length=20, required=True, label= "Şifre", widget=forms.PasswordInput(attrs={'placeholder': 'Şifre','style':"text-align: center;"}))  
    confirm_password =  forms.CharField(max_length=20, required=True, label= "Şifre(Tekrar)", widget=forms.PasswordInput(attrs={'placeholder': 'Şifre(Tekrar)','style':"text-align: center;"}))
    first_name = forms.CharField(max_length = 20, required=True, label='İsim',widget=forms.TextInput(attrs={'placeholder': 'İsim','style':"text-align: center;"}))
    last_name = forms.CharField(max_length = 20, required=True, label='Soyisim',widget=forms.TextInput(attrs={'placeholder': 'Soyisim','style':"text-align: center;"}))
    email =  forms.EmailField(max_length = 50, required=True, label='E-mail',widget=forms.TextInput(attrs={'placeholder': 'E-mail','style':"text-align: center;"}))
    
    
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
    username = forms.CharField(max_length=20, required=False, label = "Kullanıcı Adı", widget=forms.TextInput(attrs={'placeholder': 'Kullanıcı Adı', 'style':"text-align: center;"} ))
    password = forms.CharField(max_length=20, required=False, label = "Şifre", widget=forms.PasswordInput(attrs={'placeholder': 'Şifre','style':"text-align: center;"}))




class DoctorRegisterForm(forms.ModelForm):
    class Meta:
        model = RegisterDoctor
        fields = ['name','surname','email','password','phone_number','address', 'gender','department','degree','birth_date']
        widgets = {
            'password': forms.PasswordInput(),
            'birth_date': forms.DateInput(format=('%m/%d/%Y'), attrs={'class':'form-control', 'placeholder':'Select a date', 'type':'date'}),
        }
        

class DoctorLoginForm(forms.ModelForm):
    class Meta:
        model = DoctorLogin
        fields = ['email', 'password']
        widgets = {
            'password': forms.PasswordInput(),
        }