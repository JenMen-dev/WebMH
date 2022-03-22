from django.contrib import admin
from .models import Tratamiento

# Register your models here.

class TratamientoAdmin(admin.ModelAdmin):
    readonly_fileds=('created','updated')


admin.site.register(Tratamiento, TratamientoAdmin)


