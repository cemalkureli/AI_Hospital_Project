from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
import requests
from bs4 import BeautifulSoup
from gp1.forms import ContactForm
from django.core.mail import send_mail
from gp1_project import settings
from django.contrib import messages
import datetime
from user.models import RegisterDoctor



# from .models import Complaint

# Create your views here.

def show_article(request):
    
    url = request.GET.get('url')

    response = requests.get(url)
    html = response.text

    soup = BeautifulSoup(html, 'html.parser')
    article_content = soup.find('div', class_='article-content')

    return render(request, 'article.html', {'article_content': article_content})



def home(request):
    return render(request,"home.html")

def about(request):
    form = ContactForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        name = form.cleaned_data['name']
        surname = form.cleaned_data['surname']
        full_name = f"İsim-Soyisim: {name} {surname}\n"
        subject = f"{name} {surname} İsimli Hastanın Şikayeti"
        from_email = form.cleaned_data['email']
        from_email_str = f"Gönderen: {form.cleaned_data['email']}"
        to_email = settings.EMAIL_HOST_USER
        message = f"\nŞikayet: {form.cleaned_data['message']}\n"
        message_send = "Şikayetiniz Başarıyla Alınmıştır. En yakın sürede iletişime geçilecektir. İyi günler dileriz.\n\nAlınan Şikayetin İçeriği:\n"
        time = datetime.datetime.now()
        time_print = f"Tarih: {str(time.day)}/{str(time.month)}/{str(time.year)}\t\tSaat: {str(time.hour)}:{str(time.minute)}:{str(time.second)}"
        body = {
            'message_send': message_send,
            'name-surname': full_name,
            'email_str' : from_email_str,
            'message': message,
            'time': time_print,
           }
        all_message = '\n'.join(body.values())
        send_mail(subject,all_message,to_email,[from_email])
        messages.success(request, "Mesajınız gönderilmiştir. En yakın sürede iletişime geçilecektir. İyi günler dileriz.")
        return redirect('about')

    return render(request, 'about.html', {'form': form})

def categories(request):
    return render(request,"categories.html")

def doctors(request):
    doctors = RegisterDoctor.objects.all()
    context = {
        'doctors': doctors
    }
    return render(request,"doctors.html",context)


@login_required(login_url="user:login")
def appointment(request):
    return render(request,"appointment.html")


def complaints(request):
    import pickle
    mymodel = pickle.load(open("templates/pickle_folder/hasta_yorum.pickle","rb"))
    sentence = (str(request.POST.get("complaint"))).lower()

    doctors_of_categories = []

    kategori = mymodel.predict([sentence])
    dictionary = {0 : 'Kulak Burun Boğaz (KBB)', 1 :'Enfeksiyon Hastalıkları', 2 :'Beslenme ve Diyetetik Diyetisyen',
                3 :'Göz Hastalıkları', 4 : 'Onkoloji', 5 :'Kadın Hastalıkları ve Doğum', 6 :'Psikiyatri', 
                7 :'Ortopedi ve Travmatoloji', 8 :'Kardiyoloji', 9 :'Beyin ve Sinir Cerrahisi',10 :'Fiziksel Tıp ve Rehabilitasyon', 
                11 :'Göğüs Hastalıkları', 12 :'Dermatoloji', 13 :'İç Hastalıkları',14 :'Çocuk Hastalığı ve Hastalıkları', 15 :'Diş Hekimliği', 
                16 :'Üroloji'}
    category_name =dictionary.get(*kategori)

    if category_name:
        for doctor in RegisterDoctor.objects.filter(department=category_name):
            print(doctor)
            doctors_of_categories.append(doctor)

    context = {
        "machine_translate" : category_name,
        "doctors_of_categories": doctors_of_categories,

        }
    if request.method == "GET" or sentence == "":
        return render(request,"complaints.html",{})
    else:
        return render(request,"complaints.html",context)
   
    
    
