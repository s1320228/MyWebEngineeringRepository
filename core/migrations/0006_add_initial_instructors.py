from django.db import migrations


def add_instructors(apps, schema_editor):
    Instructor = apps.get_model("core", "Instructor")

    names = [
        "Alice",
        "Bob",
        "Charlie",
        "David",
        "Emma",
        "Kenta",
    ]

    for name in names:
        Instructor.objects.get_or_create(name=name)


def remove_instructors(apps, schema_editor):
    Instructor = apps.get_model("core", "Instructor")
    Instructor.objects.filter(
        name__in=[
            "Alice",
            "Bob",
            "Charlie",
            "David",
            "Emma",
            "Kenta",
        ]
    ).delete()


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0005_availabledate"),
    ]

    operations = [
        migrations.RunPython(
            add_instructors,
            remove_instructors,
        ),
    ]