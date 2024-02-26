from django.contrib import admin

# Register your models here.

from .models import Student, Portfolio, Project

admin.site.register(Student)
admin.site.register(Portfolio)
admin.site.register(Project)