from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TeamViewSet, MemberViewSet

router = DefaultRouter()
router.register(r'teams', TeamViewSet)
router.register(r'members', MemberViewSet)

urlpatterns = [
    path('', include(router.urls)),
]