from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TeamMemberView, ContactPageView

router = DefaultRouter()
router.register('member', TeamMemberView)
router.register('contacts', ContactPageView)

urlpatterns = [
    path('v1/', include(router.urls))
]