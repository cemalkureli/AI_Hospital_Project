from django.shortcuts import render,HttpResponse
from django.contrib.auth.decorators import login_required
import requests
from bs4 import BeautifulSoup

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
    return render(request,"about.html")

def categories(request):
    return render(request,"categories.html")

def doctors(request):
    return render(request,"doctors.html")

@login_required(login_url="user:login")
def appointment(request):
    return render(request,"appointment.html")

def complaints(request):
    import pickle
    mymodel = pickle.load(open("templates/pickle_folder/hasta_yorum.pickle","rb"))
    sentence = (str(request.POST.get("complaint"))).lower()

    kategori = mymodel.predict([sentence])
    dictionary = {0 : 'Kulak Burun Boğaz (KBB)', 1 :'Enfeksiyon Hastalıkları', 2 :'Beslenme ve Diyetetik Diyetisyen',
                3 :'Göz Hastalıkları', 4 : 'Onkoloji', 5 :'Kadın Hastalıkları ve Doğum', 6 :'Psikiyatri', 
                7 :'Ortopedi ve Travmatoloji', 8 :'Kardiyoloji', 9 :'Beyin ve Sinir Cerrahisi',10 :'Fiziksel Tıp ve Rehabilitasyon', 
                11 :'Göğüs Hastalıkları', 12 :'Dermatoloji', 13 :'İç Hastalıkları',14 :'Çocuk Hastalığı ve Hastalıkları', 15 :'Diş Hekimliği', 
                16 :'Üroloji'}
    category_name =dictionary.get(*kategori)
    context = {
        "machine_translate" : category_name,
        }
    if request.method == "GET" or sentence == "":
        return render(request,"complaints.html",{})
    else:
        return render(request,"complaints.html",context)
   
    
    
