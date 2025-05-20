from django.contrib import admin
from . import views
from django.contrib.auth import views as auth_views
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
# from users import views as user_views
from .views import index, onas, reviews, home, OrderCreateView, ReviewsCreateView, ProductDetailView,  GoogSearchResultView, UserOrdersListView


urlpatterns = [
    path('', index, name="index"),
    path('reviews/', reviews, name='reviews'),
    path('onas/', onas, name='onas'),
    path('post/new/', ReviewsCreateView.as_view(), name='reviews-create'),
    path('product/<int:pk>/', ProductDetailView.as_view(), name='goog-detail'),
    path('catalog/', reviews, name='catalog'),
    path('search/', GoogSearchResultView.as_view(), name='search'),
    path('orders/', home, name='orders-list'),
    path('googtypeofservice-data/', views.goog_typeofservice_data, name='goog_typeofservice_data'),
    path('googtypeofservice-chart/', views.goog_typeofservice_chart, name='goog_typeofservice_chart'),
    path('googcount-data/', views.goog_count_data, name='goog_count_data'),
    path('googcount-chart/', views.goog_count_chart, name='goog_count_chart'),
    path('orders/new/<int:pk>/', OrderCreateView.as_view(), name='orders-create'),
]