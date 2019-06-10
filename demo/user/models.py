from django.db import models

# Create your models here.


class User(models.Model):

    name = models.CharField(max_length=128, unique=True)
    password = models.CharField(max_length=256)
    email = models.EmailField(unique=True)
    common_store = models.CharField(max_length=128)

    def __str__(self):
        return self.name
