from django.contrib import admin
from .models import Product, Category


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ['name',]} # автоматически заполняемые поля


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'price', 
                    'available', 'created', 'updated', 'discount']
    list_filter = ['available', 'created', 'updated'] # сортировка по полям
    list_editable = ['price', 'available', 'discount'] # поля, редактируемые после создания продукта 
    prepopulated_fields = {'slug': ['name',]} # автоматически заполняемые поля



