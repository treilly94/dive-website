"""
This Module contains the tests for the pages app
"""
from django.test import TestCase
from django.urls import reverse

from .models import Location


def create_site(location_name):

    return Location.objects.create(location_name=location_name)


class RenderTests(TestCase):
    def test_index_page(self):
        url = reverse('sites:index')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'sites/index.html')
        self.assertContains(response, 'Fresh water sites')
        self.assertContains(response, 'Salt water sites')

    def test_detail_page(self):
        site = create_site("Trefor Pier")
        url = reverse('sites:detail', args=(site.id,))
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'sites/detail.html')
        self.assertContains(response, site.location_name)
