import csv
from pathlib import Path

from django.conf import settings
from rugby.models import Position, RugbyPlayer


POSITIONS = [
    ("Tight Head Prop", True),
    ("Hooker", True),
    ("Loose Head Prop", True),
    ("Second Row", False),
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


def run():
    # get_or_create makes this script safe to run more than once.
    for position_name, is_specialist in POSITIONS:
        Position.objects.get_or_create(
            name=position_name,
            defaults={"specialist": is_specialist},
        )

    csv_path = Path(settings.BASE_DIR) / "data" / "rugby_players.csv"
    if not csv_path.exists():
        print(f"CSV file not found: {csv_path}")
        return

    added = 0
    with csv_path.open(newline="", encoding="utf-8-sig") as csv_file:
        for row in csv.DictReader(csv_file):
            player, created = RugbyPlayer.objects.get_or_create(
                first_name=row["first_name"].strip(),
                last_name=row["last_name"].strip(),
                team=row["team"].strip(),
            )
            if created:
                added += 1

            position_names = [
                name.strip() for name in row["positions"].split("|") if name.strip()
            ]
            for position_name in position_names:
                position = Position.objects.get(name=position_name)
                player.positions.add(position)

    print(f"Rugby data loaded. New players added: {added}")
