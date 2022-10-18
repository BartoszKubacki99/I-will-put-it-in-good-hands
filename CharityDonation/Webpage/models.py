from datetime import datetime

from django.db import models
from django.core.validators import RegexValidator
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db import models
from django.utils.translation import ugettext_lazy as _


ORGANIZATIONS = [
    (1, 'zbiórka lokalna'),
    (2, 'organizacja porządkowa'),
    (3, 'fundacja')

]


class CustomUserManager(BaseUserManager):
    def create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError(_('Musisz mieć email'))
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError(_('Superuser must have is_staff=True.'))
        if extra_fields.get('is_superuser') is not True:
            raise ValueError(_('Superuser must have is_superuser=True.'))
        return self.create_user(email, password, **extra_fields)

class CustomUser(AbstractUser):
    username = None
    email = models.EmailField(_('email address'), unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.email


class Category(models.Model):
    name = models.CharField(max_length=64, unique=True)

    def __str__(self):
        return self.name


class Institution(models.Model):
    name = models.CharField(max_length=64)
    description = models.TextField()
    type = models.IntegerField(choices=ORGANIZATIONS, default=1)
    categories = models.ManyToManyField(Category)

    def __str__(self):
        return self.name


class Donation(models.Model):
    quantity = models.IntegerField()
    categories = models.ManyToManyField(Category)
    institution = models.ForeignKey(Institution, on_delete=models.CASCADE)
    address = models.CharField(max_length=120)
    phone_number_regex = RegexValidator(regex=r'^[0-9]+$', message=('Podaj właściwy numer telefonu w formacie np: "123456789"'))
    phone_number = models.CharField(validators=[phone_number_regex], max_length=12, verbose_name='phone number')
    city = models.CharField(max_length=64)
    zip_code_regex = RegexValidator(regex=r'^[0-9]+$', message=('Podaj kod pocztowy np.:"44-444"'))
    zip_code = models.CharField(validators=[zip_code_regex], max_length=6, verbose_name='zip code')
    pick_up_date = models.DateField()
    pick_up_time = models.DateTimeField()
    pick_up_comment = models.CharField(max_length=244)
    user = models.ForeignKey(CustomUser, null=True, on_delete=models.CASCADE)
