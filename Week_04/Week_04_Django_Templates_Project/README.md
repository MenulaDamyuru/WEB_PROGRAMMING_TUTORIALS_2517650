# Week 04 – Django Templates and ORM

This project follows the supplied Week 04 handout. It demonstrates:
- Django ORM queries (`all()`, `get()`) and a many-to-many relationship.
- URL routing, including an integer `student_id` path converter.
- Rendering templates with context data.
- Template variables, filters, loops, URL tags, and template inheritance.
- A student detail page and a 404 response for an unknown student.

The supplied handout ZIP contained the tutorial document and screenshots, but no starter source code or student database. This project therefore includes a small sample dataset (three students and three modules) so the pages work immediately.

## 1. Open the project

Open this folder in VS Code and open a terminal in the same folder as `manage.py`.

## 2. Create and activate a virtual environment (Windows PowerShell)

```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
```

If PowerShell blocks activation, use:
```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
.\venv\Scripts\Activate.ps1
```

## 3. Install Django and create the database

```powershell
pip install -r requirements.txt
python manage.py migrate
```

The migrations create the tables and insert sample student/module records.

## 4. Run the website

```powershell
python manage.py runserver
```

Open:
- Home page: http://127.0.0.1:8000/
- Student detail example: http://127.0.0.1:8000/myApp/1/
- Admin page: http://127.0.0.1:8000/admin/

To stop the server, press `Ctrl + C` in the terminal.

## 5. Optional: create an admin account

In a separate terminal (or after stopping the server):
```powershell
python manage.py createsuperuser
```

Follow the prompts, then sign in at `/admin/`.

## 6. Test the required URL paths

- `/` displays the student list.
- `/myApp/1/` displays the first student's details and modules.
- `/myApp/999/` returns a 404 because that student ID does not exist.
- `/bob/` returns a 404 because no URL pattern matches it.

## 7. Test ORM queries in the Django shell

```powershell
python manage.py shell
```

Then enter:
```python
from myApp.models import Student

students = Student.objects.all()
student = students[0]
print(student.firstName)

student = Student.objects.get(id=2)
print(student.firstName)

students_age_19 = Student.objects.filter(age=19)
print(students_age_19)

student = Student.objects.get(id=1)
modules = student.modules.all()
for module in modules:
    print(f"{module.code.upper()} {module.name.capitalize()}")
```

Exit the shell with `exit()`.

## GitHub upload

From the root of your `WEB_PROGRAMMING_TUTORIALS` repository, run:

```powershell
git status
git add Week_04
git status
git commit -m "Add Week 04 Django templates project"
git push origin main
```

Only stage `Week_04`; do not use `git add .` if you want to avoid including unrelated files.
