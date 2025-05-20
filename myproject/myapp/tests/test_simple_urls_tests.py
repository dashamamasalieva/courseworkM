from unittest import skip
from django.test import TestCase
from django.urls import reverse


class SimpleTests(TestCase):
    def test_home_page_status_code(self):
        url = reverse('blog-home')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_home_template_used(self):
        url = reverse('blog-home')
        response = self.client.get(url)
        self.assertTemplateUsed(response, 'blog/index.html')
