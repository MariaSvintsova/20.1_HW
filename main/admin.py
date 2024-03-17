from django.contrib import admin
from main.models import Category, Product

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')

admin.site.register(Category, CategoryAdmin)

class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'price_per_unit', 'category')
    list_filter = ['category']
    search_fields = ('name', 'description')

admin.site.register(Product, ProductAdmin)


#  filter the result by category, as well as search by name and description