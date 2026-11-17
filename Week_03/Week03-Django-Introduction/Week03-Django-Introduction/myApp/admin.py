from django.contrib import admin

from .models import Module, Student

# Registering the models makes them editable in the Django admin site.
# (The decorator form is used below, so no plain register() calls here.)


@admin.register(Module)
class ModuleAdmin(admin.ModelAdmin):
    list_display = ("code", "name")
    search_fields = ("code", "name")


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ("id", "firstName", "lastName", "age", "email", "enrolmentDate")
    list_filter = ("modules",)
    search_fields = ("firstName", "lastName", "email")
