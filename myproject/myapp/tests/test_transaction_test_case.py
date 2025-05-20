from unittest import skip
from django.test import TransactionTestCase
from myapp.models import Goog


class WidgetTransactionTestCase(TransactionTestCase):
    def test_widget_creation(self):
        Goog.objects.create(title='Анестезия', price=100)
        Goog.objects.create(title='Консультация', price=120)
        self.assertEqual(Goog.objects.count(), 2)
