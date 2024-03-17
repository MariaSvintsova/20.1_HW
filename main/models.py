from django.db import models

NULLABLE = {'blank': True, 'null': True}


class Product(models.Model):
    name = models.CharField(max_length=100, verbose_name='Name')
    description = models.TextField()
    image = models.ImageField(upload_to='products/', verbose_name='Photo', **NULLABLE)
    category = models.CharField()
    price_per_unit = models.IntegerField()
    creation_date = models.DateTimeField()
    last_modified_date = models.DateTimeField()


    def __str__(self):
        return f"{self.name} {self.description}"

    class Meta:
        verbose_name = 'Products:)'
        verbose_name_plural = 'Usual products'
        ordering = ['description']


class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name='Name')
    description = models.TextField()

    def __str__(self):
        return f"{self.name} {self.description}"

    class Meta:
        verbose_name = 'Categories'
        verbose_name_plural = 'All categories'
        ordering = ['description']



# пароль: oldgwcowh1