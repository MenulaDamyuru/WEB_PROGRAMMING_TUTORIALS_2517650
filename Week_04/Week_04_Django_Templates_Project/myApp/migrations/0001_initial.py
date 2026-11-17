from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True
    dependencies = []
    operations = [
        migrations.CreateModel(
            name="Module",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("code", models.CharField(max_length=20)),
                ("name", models.CharField(max_length=120)),
            ],
        ),
        migrations.CreateModel(
            name="Student",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("firstName", models.CharField(max_length=60)),
                ("lastName", models.CharField(max_length=60)),
                ("age", models.PositiveIntegerField()),
                ("modules", models.ManyToManyField(blank=True, related_name="students", to="myApp.module")),
            ],
        ),
    ]
