# Week 03 - Django Introduction

This project follows the Week 03 handout. It creates a Django project with one app,
models Rugby Players and Positions with a many-to-many relationship, registers
both models in Django Admin, and imports example CSV data.

## 1. Open the project folder

Open the `Week_03` folder in VS Code. Open the terminal in that folder.

## 2. Create and activate a virtual environment (Windows PowerShell)

```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
```

If PowerShell blocks activation, use Command Prompt and run:

```bat
venv\Scripts\activate.bat
```

## 3. Install packages

```powershell
python -m pip install -r requirements.txt
```

## 4. Create database tables

```powershell
python manage.py makemigrations rugby
python manage.py migrate
```

## 5. Load sample Rugby data

The CSV is in `data/rugby_players.csv`. Run:

```powershell
python manage.py runscript load_rugby_data
```

The script creates the 14 positions and adds sample players. It uses `get_or_create`
so running it again does not create duplicate players or positions.

## 6. Create an administrator

```powershell
python manage.py createsuperuser
```

Enter a username, email (optional) and password.

## 7. Run the website

```powershell
python manage.py runserver
```

Open:
- Main page: http://127.0.0.1:8000/
- Admin page: http://127.0.0.1:8000/admin/

Log in to Admin to add, edit and assign positions to Rugby Players.

## Models and relationship

- `RugbyPlayer` stores first name, last name and team.
- `Position` stores the position name and whether it is marked as specialist.
- `RugbyPlayer.positions` is a `ManyToManyField`, because a player may play
  more than one position and a position may be assigned to multiple players.
- The handout marks Tight Head Prop, Hooker and Loose Head Prop as specialist.
  The `specialist` field records that classification in the database.

Note: The handout describes specialist positions as restricted for safety. This
starter project labels those positions as specialist in the data model; it does
not implement an eligibility/qualification workflow that blocks assignments.

## GitHub upload

From the repository root (`WEB_PROGRAMMING_TUTORIALS`), add only this folder:

```powershell
git add Week_03
git status
git commit -m "Add Week 03 Django rugby project"
git push origin main
```

Check `git status` before committing to ensure only Week_03 files are staged.
The `venv/`, Python cache files and `db.sqlite3` are excluded by `.gitignore`.

## Notes about the supplied Week 03 ZIP

The supplied handout references `data/students.csv` and `data/pet_data.csv`,
but those CSV files are not included in the uploaded ZIP. The Rugby task asks
you to create a CSV, so this project includes its own example
`data/rugby_players.csv`.
