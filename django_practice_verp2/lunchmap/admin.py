from django.contrib import admin
from .models import Category, Shop

admin.site.register(Category)
admin.site.register(Shop)


# python manage.py createsuperuser
# python manage.py runserver
# http://localhost:8000/admin
