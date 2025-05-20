from django.test import TestCase
from myapp.models import Goog


class GoogModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        Goog.objects.create(title='Консультация',description='Болит зуб', price='100')

    def test_first_name_label(self):
        goog = Goog.objects.get(id=1)
        field_label = goog._meta.get_field('title').verbose_name
        self.assertEqual(field_label, 'Наименование')

    def test_phone_label(self):
        goog = Goog.objects.get(id=1)
        field_label = goog._meta.get_field('description').verbose_name
        self.assertEqual(field_label, 'Описание')

    def test_surname_max_length(self):
        goog = Goog.objects.get(id=1)
        max_length = goog._meta.get_field('price').max_length
        self.assertEqual(max_length, 50)
