import pytest
from django.core.exceptions import ValidationError
from django.utils import timezone

from core.models import Item


@pytest.mark.django_db
class TestItemModel:
    """Test suite for the Item model."""

    def test_item_creation_with_required_fields(self):
        """Test that an Item can be created with only required fields."""
        item = Item.objects.create(name="Test Item")
        assert item.id is not None
        assert item.name == "Test Item"

    def test_item_name_max_length_validation(self):
        """Test that name field enforces max_length of 200 characters."""
        long_name = "a" * 201
        item = Item(name=long_name)
        with pytest.raises(ValidationError):
            item.full_clean()

    def test_item_name_at_max_length_is_valid(self):
        """Test that name field accepts exactly 200 characters."""
        max_name = "a" * 200
        item = Item(name=max_name)
        item.full_clean()
        assert item.name == max_name

    def test_item_description_defaults_to_empty_string(self):
        """Test that description field defaults to empty string."""
        item = Item.objects.create(name="Test Item")
        assert item.description == ""

    def test_item_description_can_be_blank(self):
        """Test that description field accepts blank values."""
        item = Item(name="Test Item", description="")
        item.full_clean()
        assert item.description == ""

    def test_item_is_active_defaults_to_true(self):
        """Test that is_active field defaults to True."""
        item = Item.objects.create(name="Test Item")
        assert item.is_active is True

    def test_item_is_active_can_be_set_to_false(self):
        """Test that is_active field can be set to False."""
        item = Item.objects.create(name="Test Item", is_active=False)
        assert item.is_active is False

    def test_item_created_at_auto_generated_on_creation(self):
        """Test that created_at is automatically set when item is created."""
        before_creation = timezone.now()
        item = Item.objects.create(name="Test Item")
        after_creation = timezone.now()

        assert item.created_at is not None
        assert before_creation <= item.created_at <= after_creation

    def test_item_updated_at_auto_generated_on_creation(self):
        """Test that updated_at is automatically set when item is created."""
        before_creation = timezone.now()
        item = Item.objects.create(name="Test Item")
        after_creation = timezone.now()

        assert item.updated_at is not None
        assert before_creation <= item.updated_at <= after_creation

    def test_item_created_at_unchanged_on_update(self):
        """Test that created_at remains unchanged when item is updated."""
        item = Item.objects.create(name="Test Item")
        original_created_at = item.created_at

        item.name = "Updated Item"
        item.save()

        assert item.created_at == original_created_at

    def test_item_updated_at_changes_on_update(self):
        """Test that updated_at changes when item is updated."""
        item = Item.objects.create(name="Test Item")
        original_updated_at = item.updated_at

        import time

        time.sleep(0.01)

        item.name = "Updated Item"
        item.save()

        assert item.updated_at > original_updated_at

    def test_item_str_method_returns_name(self):
        """Test that __str__ method returns the item's name."""
        item = Item.objects.create(name="Test Item")
        assert str(item) == "Test Item"

    def test_item_str_method_with_special_characters(self):
        """Test that __str__ method handles special characters in name."""
        item = Item.objects.create(name="Test Item with émojis 🎉 and symbols @#$")
        assert str(item) == "Test Item with émojis 🎉 and symbols @#$"

    def test_item_ordering_by_created_at_descending(self):
        """Test that items are ordered by created_at in descending order by default."""
        import time

        item1 = Item.objects.create(name="First Item")
        time.sleep(0.01)
        item2 = Item.objects.create(name="Second Item")
        time.sleep(0.01)
        item3 = Item.objects.create(name="Third Item")

        items = list(Item.objects.all())
        assert items == [item3, item2, item1]

    def test_item_meta_verbose_name(self):
        """Test that Meta verbose_name is set correctly."""
        assert Item._meta.verbose_name == "item"

    def test_item_meta_verbose_name_plural(self):
        """Test that Meta verbose_name_plural is set correctly."""
        assert Item._meta.verbose_name_plural == "items"

    def test_item_indexes_exist(self):
        """Test that database indexes are defined on the model."""
        index_names = [index.name for index in Item._meta.indexes]
        assert "item_name_idx" in index_names
        assert "item_is_active_idx" in index_names
        assert "item_created_at_idx" in index_names
