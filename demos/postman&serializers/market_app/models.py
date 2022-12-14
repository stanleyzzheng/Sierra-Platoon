from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class AppUser(AbstractUser):

    email = models.EmailField(verbose_name="email address", unique=True, max_length=255)

    USERNAME_FIELD = "email"

    REQUIRED_FIELDS = []


class Category(models.Model):

    title = models.CharField(max_length=250, null=False)

    description = models.CharField(max_length=250, blank=True)


class Item(models.Model):
    title = models.CharField(max_length=250, null=False)

    description = models.CharField(max_length=250, blank=True)

    price = models.DecimalField(decimal_places=2, max_digits=6)

    category = models.ForeignKey(
        "Category", related_name="items", on_delete=models.CASCADE
    )

    def __str__(self) -> str:
        return self.title
