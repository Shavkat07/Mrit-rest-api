from django.contrib import admin

from portfolio.models import Portfolio, PortfolioCategory, PortfolioImage

# Register your models here.
admin.site.register([Portfolio, PortfolioCategory, PortfolioImage])