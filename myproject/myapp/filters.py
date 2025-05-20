import django_filters
from .models import Goog, Orders


class PostFilter(django_filters.FilterSet):
    title = django_filters.CharFilter(field_name='title')
    price = django_filters.CharFilter(field_name='price')

    class Meta:
        model = Goog
        fields = ['title', 'price']


class OrdersFilter(django_filters.FilterSet):

    class Meta:
        model = Orders
        fields = {
            'owner',
            'stat',
            'created',
        }