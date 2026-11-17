from django.contrib import admin
from .models import Module, Student

@admin.register(Module)
class ModuleAdmin(admin.ModelAdmin):
    list_display = ("code", "name")
    search_fields = ("code", "name")

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ("firstName", "lastName", "age")
    search_fields = ("firstName", "lastName")
    filter_horizontal = ("modules",)
