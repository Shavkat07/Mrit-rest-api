from django.shortcuts import render
from rest_framework.viewsets import ReadOnlyModelViewSet

from portfolio.models import Portfolio
from portfolio.serializers import PortfolioSerializer


# Create your views here.


class PortfolioView(ReadOnlyModelViewSet):
    queryset = Portfolio.objects.all()
    serializer_class = PortfolioSerializer
