from django.contrib import admin
from .models import Year, Branch, Subject, Module

admin.site.register(Year)
admin.site.register(Branch)
admin.site.register(Subject)
admin.site.register(Module)