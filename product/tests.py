from django.test import TestCase

from .models import Category

# Create your tests here.


class TestCategoryModel(TestCase):
    def test_string_representation(self):
        category = Category(name="Test Category")
        self.assertEqual(str(category), category.name)
