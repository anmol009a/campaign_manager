from rest_framework.routers import DefaultRouter
from .views import AgentViewSet, CampaignViewSet, CampaignResultViewSet

router = DefaultRouter()
router.register('agents', AgentViewSet, basename='agent')
router.register('campaigns', CampaignViewSet, basename='campaign')
router.register('results', CampaignResultViewSet, basename='campaignresult')

urlpatterns = router.urls
