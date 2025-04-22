from django.test import TestCase
from django.urls import reverse


class RunLeaderboard(TestCase):
    url = reverse("runs")

    def test_access_runs_view(self):
        response = self.client.get(self.url)
        assert response.status_code == 200
