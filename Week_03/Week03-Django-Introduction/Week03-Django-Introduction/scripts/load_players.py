"""Import the rugby squad from players.csv.

    python manage.py runscript load_players
"""
from csv import DictReader
from pathlib import Path

from django.conf import settings

from rugby.models import Player, Position

# Specialist positions are in bold in the tutorial brief: only the players
# allocated to them may play there for safety reasons.
POSITIONS = [
    ("Tight Head Prop", True),
    ("Hooker", True),
    ("Loose Head Prop", True),
    ("Second Row", True),
    ("Open Side Flanker", False),
    ("Blind Side Flanker", False),
    ("Number 8", False),
    ("Scrum Half", False),
    ("Fly Half", False),
    ("Inside Centre", False),
    ("Outside Centre", False),
    ("Left Wing", False),
    ("Right Wing", False),
    ("Full Back", False),
]

ALREADY_LOADED = """
Player data already loaded - exiting.
Delete db.sqlite3, run `python manage.py migrate` and rerun to reload."""


def run():
    if Player.objects.exists() or Position.objects.exists():
        print("Player data already loaded...exiting.")
        print(ALREADY_LOADED)
        return

    print("Creating position data")
    for name, specialist in POSITIONS:
        Position(name=name, specialist=specialist).save()

    print("Loading player data")
    csv_path = Path(settings.BASE_DIR) / "players.csv"
    with csv_path.open(newline="", encoding="utf-8") as handle:
        for row in DictReader(handle):
            player = Player()
            player.firstName = row["fname"]
            player.lastName = row["lname"]
            player.squadNumber = row["squad number"]
            player.save()
            for pos_name in [n for n in row["positions"].split("|") if n.strip()]:
                player.positions.add(Position.objects.get(name=pos_name.strip()))
            player.save()

    print(f"Loaded {Player.objects.count()} players and {Position.objects.count()} positions")
