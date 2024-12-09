from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
# from users import views as user_views
from .views import index, reviews, ReviewsCreateView, ProductDetailView

urlpatterns = [
    path('', index, name="blog-home"),
    path('reviews/', reviews, name='reviews'),
    path('post/new/', ReviewsCreateView.as_view(), name='reviews-create'),
    path('product/<int:pk>/', ProductDetailView.as_view(), name='goog-detail'),
]
