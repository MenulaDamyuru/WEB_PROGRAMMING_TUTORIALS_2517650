from django.db import migrations


def add_sample_data(apps, schema_editor):
    Student = apps.get_model("myApp", "Student")
    Module = apps.get_model("myApp", "Module")

    programming = Module.objects.create(code="MOD003212", name="Introduction to Programming")
    database = Module.objects.create(code="MOD003218", name="Database Systems")
    web = Module.objects.create(code="MOD003219", name="Web Programming")

    connie = Student.objects.create(firstName="Connie", lastName="James", age=19)
    joshua = Student.objects.create(firstName="Joshua", lastName="Perera", age=20)
    amara = Student.objects.create(firstName="Amara", lastName="Silva", age=18)
    connie.modules.add(programming, database)
    joshua.modules.add(programming, web)
    amara.modules.add(database, web)


def remove_sample_data(apps, schema_editor):
    Student = apps.get_model("myApp", "Student")
    Module = apps.get_model("myApp", "Module")
    Student.objects.all().delete()
    Module.objects.all().delete()


class Migration(migrations.Migration):
    dependencies = [("myApp", "0001_initial")]
    operations = [migrations.RunPython(add_sample_data, remove_sample_data)]
