from django.db import models
from django.utils.text import slugify
from mptt.models import MPTTModel, TreeForeignKey


class ActiveProductManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(product_line__is_active=True)


class Category(MPTTModel):
    name = models.CharField(
        max_length=100,
        unique=True,
    )
    slug = models.SlugField(max_length=100, unique=True, blank=True)
    parent = TreeForeignKey(
        "self", on_delete=models.PROTECT, null=True, blank=True, related_name="children"
    )

    class MPTTMeta:
        order_insertion_by = ["name"]

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name


class Brand(models.Model):
    name = models.CharField(
        max_length=100,
        unique=True,
    )
    slug = models.SlugField(max_length=100, unique=True, blank=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(
        max_length=100,
        unique=True,
    )
    slug = models.SlugField(max_length=100, unique=True, blank=True)
    description = models.TextField(
        blank=True,
        null=True,
    )
    is_digital = models.BooleanField(default=False)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    category = TreeForeignKey(
        Category, null=True, blank=True, on_delete=models.SET_NULL
    )

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    objects = models.Manager()
    active = ActiveProductManager()

    def __str__(self):
        return self.name


class ProductLine(models.Model):
    price = models.DecimalField(max_digits=10, decimal_places=2)
    sku = models.CharField(max_length=100, unique=True)
    stock_qty = models.IntegerField()
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, related_name="product_line"
    )
    is_active = models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.product.name
