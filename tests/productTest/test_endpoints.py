import pytest

pytestmark = pytest.mark.django_db


class TestCategoryEndpoints:
    endpoint = "/api/categories/"

    def test_get_category(self, category_factory, api_client):
        # Arrange
        category_factory()
        # Act
        response = api_client().get(self.endpoint)
        # Assert
        assert response.status_code == 200


class TestBrandEndpoints:
    endpoint = "/api/brands/"

    def test_get_brand(
        self,
        brand_factory,
        api_client,
    ):
        brand_factory()
        response = api_client().get(self.endpoint)
        assert response.status_code == 200


class TestProductEndpoints:
    endpoint = "/api/products/"

    def test_get_product(
        self,
        product_factory,
        api_client,
    ):
        product_factory()
        response = api_client().get(self.endpoint)
        assert response.status_code == 200
