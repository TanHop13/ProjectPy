from cloudinary.models import CloudinaryField
from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    avatar = CloudinaryField(null=False, default="https://res.cloudinary.com/dvzsftuep/"
                                                 "image/upload/v1718008117/e83yxveneoxzwh4ehfvu.png")


class Products(models.Model):
    name = models.CharField(max_length=255),
    description = models.CharField(max_length=255)

    def __str__(self):
        return self.name
