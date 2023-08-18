from rest_framework import serializers
from portfolio.models import Portfolio, PortfolioCategory, PortfolioImage


class PortfolioCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = PortfolioCategory
        fields = ('id', 'name')


class PortfolioImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = PortfolioImage
        fields = ('image',)


class PortfolioSerializer(serializers.ModelSerializer):
    category = PortfolioCategorySerializer()
    images = PortfolioImageSerializer(source='portfolioimage_set', many=True)
    class Meta:
        model = Portfolio
        fields = ('id', 'category', 'title', 'image', 'link',
                  'textfull', 'watches', 'like', 'images')
