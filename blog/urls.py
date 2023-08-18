from blog.views import BlogView
from django.urls import path, include
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('blog', BlogView)

urlpatterns = [
    path('v1/', include(router.urls))
]