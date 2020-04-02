from rest_framework import routers

from Snippets.views import SnippetViewSet

router = routers.DefaultRouter(trailing_slash=False)

router.register('snippets',SnippetViewSet)