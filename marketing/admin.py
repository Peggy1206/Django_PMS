from django.contrib import admin

# Register your models here.
from .models import Customer,Item,PurRecord

admin.site.register(Customer)
admin.site.register(Item)
admin.site.register(PurRecord)