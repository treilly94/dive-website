"""
This Module contains the tests for the pages app
"""
import datetime
from django.utils import timezone
from django.test import TestCase
from django.urls import reverse

from .models import Location


class RenderTests(TestCase):
    def test_index_page(self):
        url = reverse('sites:index')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'sites/index.html')
        self.assertContains(response, 'Fresh water sites')
        self.assertContains(response, 'Salt water sites')
