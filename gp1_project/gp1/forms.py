from django import forms 

class ContactForm(forms.Form):
    name = forms.CharField(max_length = 25, required=True, label='İsim')
    surname = forms.CharField(max_length = 25, required=True, label='Soyisim')
    email = forms.EmailField(required=True,max_length=50,label='Email')
    message = forms.CharField(max_length=500,required=True,widget=forms.Textarea, label='Mesajınız')

    def clean(self) -> dict[str]: 
        name = self.cleaned_data.get("name")
        surname = self.cleaned_data.get("surname")
        email = self.cleaned_data.get("email")
        message = self.cleaned_data.get("message")

        value = {
            "name" : name,
            "surname" : surname,
            "email" : email,
            "message" : message,
        }

        return value