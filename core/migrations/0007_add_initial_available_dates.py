from datetime import date

from django.db import migrations


def add_available_dates(apps, schema_editor):
    Instructor = apps.get_model("core", "Instructor")
    AvailableDate = apps.get_model("core", "AvailableDate")

    dates_by_instructor = {
        "Alice": [
            date(2026, 8, 1),
            date(2026, 8, 5),
            date(2026, 8, 10),
        ],
        "Bob": [
            date(2026, 8, 3),
            date(2026, 8, 7),
            date(2026, 8, 12),
        ],
        "Charlie": [
            date(2026, 8, 2),
            date(2026, 8, 8),
            date(2026, 8, 15),
        ],
        "David": [
            date(2026, 7, 30),
            date(2026, 8, 2),
            date(2026, 8, 5),
            date(2026, 8, 15),
        ],
        "Emma": [
            date(2026, 8, 12),
            date(2026, 8, 14),
            date(2026, 8, 22),
        ],
        "Kenta": [
            date(2026, 8, 2),
            date(2026, 8, 16),
            date(2026, 8, 22),
        ],
    }

    for instructor_name, available_dates in dates_by_instructor.items():
        try:
            instructor = Instructor.objects.get(name=instructor_name)
        except Instructor.DoesNotExist:
            continue

        for available_date in available_dates:
            AvailableDate.objects.get_or_create(
                instructor=instructor,
                date=available_date,
            )


def remove_available_dates(apps, schema_editor):
    AvailableDate = apps.get_model("core", "AvailableDate")

    dates = [
        date(2026, 7, 30),
        date(2026, 8, 1),
        date(2026, 8, 2),
        date(2026, 8, 3),
        date(2026, 8, 5),
        date(2026, 8, 7),
        date(2026, 8, 8),
        date(2026, 8, 10),
        date(2026, 8, 12),
        date(2026, 8, 14),
        date(2026, 8, 15),
        date(2026, 8, 16),
        date(2026, 8, 22),
    ]

    AvailableDate.objects.filter(date__in=dates).delete()


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0006_add_initial_instructors"),
    ]

    operations = [
        migrations.RunPython(
            add_available_dates,
            remove_available_dates,
        ),
    ]