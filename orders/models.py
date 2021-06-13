from django.db import models


# HT 8. OneToOneField, ForeignKey, ManyToManyField
class City(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    date_created = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return self.name


class Client(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100, unique=True)
    age = models.PositiveSmallIntegerField()
    product = models.ManyToManyField(Product, verbose_name='client products')
    city = models.ForeignKey(City, on_delete=models.CASCADE, verbose_name='client city')

    def __str__(self):
        return f'{self.first_name}, {self.last_name}'


class Supplier(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    city = models.OneToOneField(City, on_delete=models.CASCADE, verbose_name='supplier city')

    def __str__(self):
        return f'{self.first_name}, {self.last_name}'
