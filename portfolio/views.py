from django.shortcuts import render
from rest_framework.viewsets import ReadOnlyModelViewSet

from portfolio.models import Portfolio
from portfolio.serializers import PortfolioSerializer


# Create your views here.


class PortfolioView(ReadOnlyModelViewSet):
    queryset = Portfolio.objects.all()
    serializer_class = PortfolioSerializer

    def retrieve(self, request, *args, **kwargs):
        response = super().retrieve(request, *args, **kwargs)
        obj = self.get_object()
        obj.watches += 1
        obj.save()
        return response