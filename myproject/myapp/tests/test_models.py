from unittest import skip
from django.test import TestCase
from myapp.models import Goog


class MyModelTest(TestCase):
    def setUp(self):
        self.object = Goog.objects.create(title="Анестезия", price=100)

    def test_str_representation(self):
        self.assertEqual(str(self.object), 'Анестезия')

    def tearDown(self):
        pass
