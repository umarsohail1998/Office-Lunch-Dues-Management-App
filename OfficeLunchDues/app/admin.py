from django.contrib import admin

from .models import Employees, Record, Monthly_Record

# Register your models here.
admin.site.register(Employees)
admin.site.register(Record)
admin.site.register(Monthly_Record)
