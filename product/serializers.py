from rest_framework import serializers

from .models import Brand, Category, Product, ProductLine


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"
        read_only_fields = ("slug",)


class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = "__all__"
        read_only_fields = ("slug",)


class ProductLineSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductLine
        fields = "__all__"
        read_only_fields = ("slug",)


class ProductLineForProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductLine
        fields = ("price", "sku", "stock_qty")


class ProductSerializer(serializers.ModelSerializer):
    brand = serializers.CharField(source="brand.name", read_only=True)
    category = serializers.CharField(source="category.name", read_only=True)
    product_line = ProductLineForProductSerializer(many=True, read_only=True)

    class Meta:
        model = Product
        fields = "__all__"
        read_only_fields = ("slug",)

    def create(self, validated_data):
        brand_data = validated_data.pop("brand")
        category_data = validated_data.pop("category")
        brand, _ = Brand.objects.get_or_create(**brand_data)
        category, _ = Category.objects.get_or_create(**category_data)
        product = Product.objects.create(
            brand=brand, category=category, **validated_data
        )
        return product
