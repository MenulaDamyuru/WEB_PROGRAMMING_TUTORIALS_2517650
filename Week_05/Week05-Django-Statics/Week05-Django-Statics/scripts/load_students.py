"""Import module and student data from students.csv.

Run with django-extensions:

    python manage.py runscript load_students
"""
from csv import DictReader
from datetime import datetime, timezone
from pathlib import Path

from django.conf import settings

from myApp.models import Module, Student

DATETIME_FORMAT = "%d/%m/%Y"

MODULES = {
    "MOD002619": "Web Programming",
    "MOD002643": "Image Processing",
    "MOD002691": "Final Project",
    "MOD003212": "Introduction to Programming",
    "MOD003484": "Software Principles",
}

ALREADY_LOADED = """
Student data already loaded - exiting.
If you need to reload it, delete db.sqlite3, run `python manage.py migrate`
and then run this script again."""


def run():
    if Student.objects.exists() or Module.objects.exists():
        print("Student data already loaded...exiting.")
        print(ALREADY_LOADED)
        return

    print("Creating module data")
    for mcode, mname in MODULES.items():
        Module(code=mcode, name=mname).save()

    print("Loading student data")
    csv_path = Path(settings.BASE_DIR) / "students.csv"
    images = sorted(p.name for p in (Path(settings.BASE_DIR) / "images").glob("*.jpg"))

    with csv_path.open(newline="", encoding="utf-8") as handle:
        for index, row in enumerate(DictReader(handle)):
            stu = Student()
            stu.firstName = row["fname"]
            stu.lastName = row["lname"]
            stu.age = row["age"]
            stu.email = row["email"]
            stu.enrolmentDate = datetime.strptime(
                row["enrolment date"], DATETIME_FORMAT
            ).replace(tzinfo=timezone.utc)
            # Give every fourth student a photo so the media/static work in
            # week 05 has some data to display.
            if images and index % 4 == 0:
                stu.image = f"images/{images[(index // 4) % len(images)]}"
            stu.save()

            # Now add the module enrolments (they are stored as "CODE | CODE")
            raw_modules = row["modules"]
            for mod_name in [name for name in raw_modules.split("|") if name.strip()]:
                mod = Module.objects.get(code=mod_name.strip())
                stu.modules.add(mod)
            stu.save()

    print(f"Loaded {Student.objects.count()} students and {Module.objects.count()} modules")
