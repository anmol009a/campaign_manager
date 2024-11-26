from django.test import TestCase
from rest_framework.test import APITestCase
from rest_framework import status
from .models import Agent, Campaign

# Create your tests here.
class CampaignAPITest(APITestCase):
    def setUp(self):
        self.agent = Agent.objects.create(
            agent_name="Test Agent",
            language="English",
            voice_id="T12345"
        )

    def test_create_agent(self):
        response = self.client.post('/api/agents/', {
            "agent_name": "New Agent",
            "language": "French",
            "voice_id": "N54321"
        })
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_campaign(self):
        response = self.client.post('/api/campaigns/', {
            "campaign_name": "Test Campaign",
            "campaign_type": "Outbound",
            "phone_number": "123-456-7890",
            "status": "Running",
            "agent": self.agent.id
        })
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
