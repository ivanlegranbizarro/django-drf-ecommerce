import pytest

pytestmark = pytest.mark.django_db


class TestCategoryModel:
    def test_str_method(self, category_factory):
        # Arrange
        # Act
        x = category_factory()
        # Assert
        assert x.__str__() == x.name


class TestBrandModel:
    def test_str_method(self, brand_factory):
        # Arrange
        # Act
        x = brand_factory()
        # Assert
        assert x.__str__() == x.name


class TestProductModel:
    def test_str_method(self, product_factory):
        # Arrange
        # Act
        x = product_factory()
        # Assert
        assert x.__str__() == x.name
