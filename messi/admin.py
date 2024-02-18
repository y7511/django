from django.contrib import admin
from .models import CompanyInformation, Product, Category

admin.site.register(CompanyInformation)
admin.site.register(Product)
admin.site.register(Category)
