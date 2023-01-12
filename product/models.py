from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from mptt.models import MPTTModel, TreeForeignKey

# Create your models here.


class Category(MPTTModel):
    name = models.CharField(
        max_length=100,
        unique=True,
        validators=[MinValueValidator(3), MaxValueValidator(100)],
    )
    parent = TreeForeignKey(
        "self", on_delete=models.PROTECT, null=True, blank=True, related_name="children"
    )

    class MPTTMeta:
        order_insertion_by = ["name"]

    def __str__(self):
        return self.name


class Brand(models.Model):
    name = models.CharField(
        max_length=100,
        unique=True,
        validators=[MinValueValidator(3), MaxValueValidator(100)],
    )

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(
        max_length=100,
        unique=True,
        validators=[MinValueValidator(3), MaxValueValidator(100)],
    )
    description = models.TextField(
        blank=True,
        null=True,
        validators=[MinValueValidator(3), MaxValueValidator(1000)],
    )
    is_digital = models.BooleanField(default=False, null=True, blank=True)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    category = TreeForeignKey(
        Category, null=True, blank=True, on_delete=models.SET_NULL
    )

    def __str__(self):
        return self.name
