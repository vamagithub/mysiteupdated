from django.contrib import admin
# import your model
from .models import Thing


# setup automatic slug creation
class ThingAdmin(admin.ModelAdmin):
    model = Thing
    list_display = ('first_name', 'last_name', 'pan', 'dob', 'phone', 'user')
    prepopulated_fields = {'slug': ('pan',)}


# Register your models here.
admin.site.register(Thing, ThingAdmin)

