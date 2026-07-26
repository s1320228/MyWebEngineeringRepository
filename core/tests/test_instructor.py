import pytest
from core.models import Instructor

@pytest.mark.django_db
def test_create_instructor():
    instructor = Instructor.objects.create(
        name="Alice"
    )

    assert instructor.name == "Alice"