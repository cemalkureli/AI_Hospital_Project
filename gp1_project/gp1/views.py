from django.shortcuts import render,HttpResponse
# from .models import Complaint

# Create your views here.

def home(request):
    return render(request,"home.html")

def about(request):
    return render(request,"about.html")

def categories(request):
    return render(request,"categories.html")

def doctors(request):
    return render(request,"doctors.html")

def appointment(request):
    return render(request,"appointment.html")

def complaints(request):
    import pickle
    empty_str = ""
    mymodel = pickle.load(open("templates/pickle_folder/hasta_yorum.pickle","rb"))
    sentence = (str(request.POST.get("complaint"))).lower()
    print("asdasd",sentence)
    if sentence != empty_str:
        kategori = mymodel.predict([sentence])
        print(kategori)
        dictionary = {0 : 'Kulak Burun Boğaz (KBB)', 1 :'Enfeksiyon Hastalıkları', 2 :'Beslenme ve Diyetetik Diyetisyen',
                    3 :'Göz Hastalıkları', 4 : 'Onkoloji', 5 :'Kadın Hastalıkları ve Doğum', 6 :'Psikiyatri', 
                    7 :'Ortopedi ve Travmatoloji', 8 :'Kardiyoloji', 9 :'Beyin ve Sinir Cerrahisi',10 :'Fiziksel Tıp ve Rehabikseilitasyon', 
                    11 :'Göğüs Hastalıkları', 12 :'Dermatoloji', 13 :'İç Hastalıkları',14 :'Çocuk Hastalığı ve Hastalıkları', 15 :'Diş Hekimliği', 
                    16 :'Üroloji'}
        category_name =dictionary.get(*kategori)
        context = {
            "machine_translate" : category_name
            }
        print(category_name)
    else:
        context = {
            "machine_translate_empty" : empty_str
            }

    return render(request,"complaints.html",context)