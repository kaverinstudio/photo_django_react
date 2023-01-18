from rest_framework import routers
from .api import MainCardViewSet


router = routers.DefaultRouter()
router.register('api/main', MainCardViewSet)


urlpatterns = router.urls