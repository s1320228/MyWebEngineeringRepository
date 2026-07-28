from django.conf import settings
from django.db import models


class Instructor(models.Model):
    name = models.CharField(max_length=100)
    photo = models.ImageField(
        upload_to="instructors/",
        blank=True,
        null=True,
    )

    def __str__(self):
        return self.name


class AvailableDate(models.Model):
    instructor = models.ForeignKey(
        Instructor,
        on_delete=models.CASCADE,
        related_name="available_dates",
    )

    date = models.DateField()

    class Meta:
        ordering = ["date"]

        constraints = [
            models.UniqueConstraint(
                fields=["instructor", "date"],
                name="unique_instructor_available_date",
            )
        ]

    def __str__(self):
        return f"{self.instructor.name} - {self.date}"


class Reservation(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="reservations",
        null=True,
        blank=True,
    )

    instructor = models.ForeignKey(
        Instructor,
        on_delete=models.CASCADE,
        related_name="reservations",
    )

    customer_name = models.CharField(max_length=100)
    reservation_date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["reservation_date"]

        constraints = [
            models.UniqueConstraint(
                fields=[
                    "user",
                    "instructor",
                    "reservation_date",
                ],
                name="unique_user_instructor_reservation",
            )
        ]

    def __str__(self):
        return (
            f"{self.customer_name} - "
            f"{self.instructor.name} - "
            f"{self.reservation_date}"
        )