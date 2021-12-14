from django.contrib import admin
from .models import Country, Traveler, Bucketlist
# Register your models here.
admin.site.register(Country)
admin.site.register(Traveler)
admin.site.register(Bucketlist)