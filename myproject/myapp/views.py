from django.shortcuts import render, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
from .models import Goog, Comment, Reviews
from .filters import PostFilter


def index(request):
    tasks_all = Goog.objects.order_by('id')
    tasks = PostFilter(request.GET, queryset=tasks_all)
    context = {
        'posts': tasks,
        'title': 'Главная страница'
    }
    return render(request, 'myapp/index.html', context)


def reviews(request):
    context = {
        'reviews': Reviews.objects.all()
    }
    return render(request, 'myapp/reviews.html', context)


class ReviewsCreateView(LoginRequiredMixin, CreateView):
    model = Reviews
    fields = ['content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class ProductDetailView(DetailView):
    model = Goog