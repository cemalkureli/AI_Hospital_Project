from django.db import models
from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.


class RegisterDoctor(models.Model):

    GENDER_CHOICES = [
        ('Erkek', 'Erkek'),
        ('Kadın', 'Kadın'),
        ('Diğer', 'Diğer'),
    ]
    DEPARTMENT_CHOICES = [
        ('Dermatoloji', 'Dermatoloji'),
        ('İç Hastalıkları', 'İç Hastalıkları'),
        ('Beyin ve Sinir Cerrahisi', 'Beyin ve Sinir Cerrahisi'),
        ('Ortopedi ve Travmatoloji', 'Ortopedi ve Travmatoloji'),
        ('Kulak Burun Boğaz (KBB)', 'Kulak Burun Boğaz (KBB)'),
        ('Onkoloji', 'Onkoloji'),
        ('Çocuk Hastalığı ve Hastalıkları', 'Çocuk Hastalığı ve Hastalıkları'),
        ('Göğüs Hastalıkları', 'Göğüs Hastalıkları'),
        ('Üroloji', 'Üroloji'),
        ('Psikiyatri', 'Psikiyatri'),
        ('Kadın Hastalıkları ve Doğum', 'Kadın Hastalıkları ve Doğum'),
        ('Göz Hastalıkları', 'Göz Hastalıkları'),
        ('Fiziksel Tıp ve Rehabilitasyon', 'Fiziksel Tıp ve Rehabilitasyon'),
        ('Diş Hekimliği', 'Diş Hekimliği'),
        ('Enfeksiyon Hastalıkları', 'Enfeksiyon Hastalıkları'),
        ('Beslenme ve Diyetetik Diyetisyen', 'Beslenme ve Diyetetik Diyetisyen'),
        ('Kardiyoloji', 'Kardiyoloji'),
    ]
    DEGREE_CHOICES = [
        ('Pratisyen Dr.', 'Pratisyen Dr.'),
        ('Dr.', 'Dr.'),
        ('Uzm. Dr.', 'Uzm. Dr.'),
        ('Doc. Dr.', 'Doc. Dr.'),
        ('Op. Dr.', 'Op. Dr.'),
        ('Doc. Dr.', 'Doc. Dr.'),
        ('Prof. Dr.', 'Prof. Dr.'),
    ]

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=25, verbose_name="İsim")
    surname = models.CharField(max_length=25, verbose_name="Soyisim")
    email = models.EmailField(verbose_name="Email")
    password = models.CharField(max_length=200, verbose_name="Şifre")
    phone_number = PhoneNumberField(blank=True,max_length =13,region='TR',verbose_name="Telefon No")
    address = models.CharField(max_length=100,verbose_name="Adres")
    
    gender = models.CharField(
        max_length=10,
        choices=GENDER_CHOICES,
        verbose_name="Cinsiyet",
    )
    department = models.CharField(
        max_length=50,
        choices=DEPARTMENT_CHOICES,
        verbose_name="Bölüm",
    )
    degree = models.CharField(
        max_length=20,
        choices=DEGREE_CHOICES,
        verbose_name="Ünvan",
    )
    birth_date = models.DateField(auto_now=False, auto_now_add=False,null=True,verbose_name="Doğum Tarihi")
    
    def __str__(self):
        return f'{self.name} + {self.surname}'


class DoctorLogin(models.Model):
    email = models.EmailField(verbose_name = "Email")
    password = models.CharField(max_length=200,verbose_name = "Şifre")