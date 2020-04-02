from rest_framework import routers

from Accounts.views import UserViewSet

router = routers.DefaultRouter(trailing_slash=False)

router.register('users', UserViewSet, basename="Users")
