from unittest import skip
from django.test import TestCase, RequestFactory
from unittest.mock import Mock, patch
from myapp.models import Goog
from myapp.views import index


class GoogListViewTest(TestCase):
    def setUp(self):
        self.factory = RequestFactory()

    def test_name_list_view(self):
        Goog.objects.create(title='Консультация', price=10)
        Goog.objects.create(title='Анестезия', price=100)

        request = self.factory.get('/index/')

        mock_queryset = Mock(spec=Goog.objects.all())
        mock_queryset.return_value = [
            Mock(title='Консультация', price=10),
            Mock(title='Анестезия', price=100)
        ]

        with patch('blog.views.Goog.objects.all', mock_queryset):
            response = index(request)

        self.assertEqual(response.status_code, 200)

        # self.assertContains(response, 'Сыр', 10)
        # self.assertContains(response, 'Торт', 100)