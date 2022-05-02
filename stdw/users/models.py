from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):

    email=models.EmailField(unique=True)

    #Para reemplazar el user por el correo
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []