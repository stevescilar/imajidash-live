from django.contrib import admin
from .models import offloadedCargo
# Register your models here.


class offloadedCargoAdmin(admin.ModelAdmin):
    list_display = ['container_origin','container_number','client']
admin.site.register(offloadedCargo)

