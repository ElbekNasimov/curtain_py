from django.db import models
from users.models import CustomUser
from datetime import datetime
# Create your models here.


# Categories of products
class Category(models.Model):
    cat_name = models.CharField(max_length=20, verbose_name="Kategoriya")

    def __str__(self):
        return self.cat_name

    class Meta:
        verbose_name_plural = 'Kategoriyalar'


# where the products are
class Location(models.Model):
    loc = models.CharField(max_length=10, verbose_name="Joyi")

    def __str__(self):
        return self.loc

    class Meta:
        verbose_name_plural = 'Saqlanadigan joy'


# product unit of measure
class MeasureType(models.Model):
    m_type = models.CharField(max_length=10, default="m")

    def __str__(self):
        return self.m_type

    class Meta:
        verbose_name_plural = "O'lchov birligi"


# products
class Product(models.Model):
    author = models.ForeignKey(CustomUser, null=True, blank=True, on_delete=models.CASCADE,
                               verbose_name="Qo'shgan odam")
    category = models.ForeignKey(Category, verbose_name="Kategoriya", on_delete=models.CASCADE)
    title = models.CharField(verbose_name="Mahsulot nomi", max_length=150)
    description = models.TextField(verbose_name="Izoh")
    selling_price = models.DecimalField(verbose_name="Sotilish narxi ($)", max_digits=9, decimal_places=2)
    length = models.DecimalField(verbose_name="Uzunligi (m)", editable=True, max_digits=5, decimal_places=2)
    measure_type = models.ForeignKey(MeasureType, on_delete=models.CASCADE, verbose_name="O'lchov birligi")
    storage = models.ForeignKey(Location, on_delete=models.CASCADE, verbose_name="Joyi")
    status = models.BooleanField(default=False)
    barcode = models.CharField(max_length=100, default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.title)

    class Meta:
        verbose_name_plural = 'Mahsulotlar'


# Images of Products
class ProductImage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name="Mahsulot")
    images = models.ImageField(upload_to='product_images', verbose_name="Rasmi")

    def __str__(self):
        return f"{self.product}'s image"

    class Meta:
        verbose_name_plural = 'Mahsulotlar rasmi'


# Products cost
class Cost(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    buy_price = models.DecimalField(max_digits=12, decimal_places=3, verbose_name="Sotib olingan mnarx")
    kilo_per_metr = models.DecimalField(max_digits=7, decimal_places=3,
                                        verbose_name="Kilosiga metri", null=True, blank=True)
    price_per_metr = models.DecimalField(max_digits=7, decimal_places=3,
                                         verbose_name="Metriga yo'l kira", null=True, blank=True)
    cost_price = models.DecimalField(max_digits=7, decimal_places=3, verbose_name="Tannarx")

    def __str__(self):
        return f"{self.product} tannarx {self.cost_price}"


# Type of Money Spent
class OutlayType(models.Model):
    o_type = models.CharField(max_length=10, verbose_name="Xarajat turi")

    def __str__(self):
        return self.o_type

    class Meta:
        verbose_name_plural = "Xarajatlar Turi"


# Money Spent
class Outlay(models.Model):
    summa = models.DecimalField(max_digits=11, decimal_places=1)
    date = models.DateTimeField(default=datetime.now())
    outlay_type = models.ForeignKey(OutlayType, on_delete=models.SET_DEFAULT,
                                    verbose_name="Xarajat turi", default="Boshqalar")
    description = models.TextField(verbose_name="Izoh")

    def __str__(self):
        return f"{self.outlay_type}ga {self.summa} xarajat"

    class Meta:
        verbose_name_plural = "Xarajatlar"
