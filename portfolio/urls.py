from django.urls import path, include
from rest_framework.routers import DefaultRouter

from portfolio.views import PortfolioView

router = DefaultRouter()

router.register('portfolio', PortfolioView)

urlpatterns = [
    path('v1/', include(router.urls))
]