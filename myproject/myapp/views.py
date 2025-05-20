from django.core.checks import messages
from django.utils import timezone
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from django.db.models import Count
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
from .models import Goog, Comment, Reviews, Orders, TypeOfService, Stat
from .filters import PostFilter,OrdersFilter
from django.contrib.postgres.search import SearchVector, SearchQuery, SearchRank
from django.views.generic import ListView
from django.utils import timezone
from django.http import JsonResponse
from .forms import ProductForm


def index(request):
    tasks_all = Goog.objects.order_by('id')
    tasks = PostFilter(request.GET, queryset=tasks_all)
    context = {
        'posts': tasks,
        'title': 'Гланая страница'
    }
    return render(request, 'myapp/index.html', context)


def onas(request):
    return render(request, 'myapp/onas.html')


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


def ajax_change_status(request, pk):
    order_id = request.GET.get('id', False)
    status = Stat.objects.get(id=3)
    number = Orders.objects.filter(id=pk).update(stat=status)
    return redirect('orders-list', username=request.user)

class GoogSearchResultView(ListView):
    model = Goog
    context_object_name = 'googs'
    paginate_by = 10
    allow_empty = True
    template_name = 'myapp/articles_list.html'

    def get_queryset(self):
        query = self.request.GET.get('do')
        search_vector = SearchVector('full_description', weight='B') + SearchVector('title', weight='A')
        search_query = SearchQuery(query)
        return (
            self.model.objects.annotate(rank=SearchRank(search_vector, search_query)).filter(rank__gte=0.3).order_by(
                '-rank'))

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = f'Результаты поиска: {self.request.GET.get("do")}'
        return context


class UserOrdersListView(ListView):
    model = Orders
    context_object_name = 'orders'
    now = timezone.now()
    extra_context = {'title': 'История записей', 'now': now}

    def get_queryset(self):
        return Orders.objects.filter(owner=self.request.user).order_by('-created')


class OrderCreateView(LoginRequiredMixin, CreateView):
    form_class = ProductForm
    template_name = 'myapp/goog_forms.html'
    success_url = '/'

    def form_invalid(self, form):
        for field, errors in form.errors.items():
            for error in errors:
                messages.error(self.request, f'В поле {field} возникла ошибка: {error}')
        return super().form_invalid(form)

    def form_valid(self, form):
        form.instance.owner = self.request.user
        print(self.request)
        print(self.kwargs['pk'])
        form.instance.stat = Stat.objects.get(id=1)  # Отправлен
        form.instance.prod = Goog.objects.get(id=self.kwargs['pk'])  # Выбираем товар по pk
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super(OrderCreateView, self).get_context_data(**kwargs)
        context['header_text'] = "My Form"
        pk = self.kwargs.get('pk')
        selected_product = Goog.objects.get(id=pk)
        context['prod_info'] = f'Наименование: {selected_product.title} '
        return context


def goog_typeofservice_data(request):
    # Запрос - Выборка количества заявок по типам услуг
    result = (Orders.objects
              .values('id')
              .annotate(dcount=Count('id'))
              .order_by()
              )
    service_res = TypeOfService.objects.values('id', 'title').all()
    service = dict()
    # Выборка типов улуг
    for elem in service_res:
        service[elem['id']] = elem['title']
    labels = []
    values = []
    # Подставляю название услуги вместо её номера
    for elem in result:
        if elem['id'] in service.keys():
            labels.append(service[elem['id']])
            values.append(elem['dcount'])
    return JsonResponse({'labels': labels, 'values': values})


def goog_typeofservice_chart(request):
    return render(request, 'myapp/goog_typeofservice_chart.html')


def goog_count_data(request):
    select_data = {"d": """strftime('%%Y/%%m', created)"""}
    result = (Orders.objects
              .extra(select=select_data)
              .values("d")
              .annotate(dcount=Count("*"))
              .order_by()
              )
    print(result)
    labels = []
    values = []
    for elem in result:
        labels.append(elem['d'])
        values.append(elem['dcount'])
    return JsonResponse({'labels': labels, 'values': values})


def goog_count_chart(request):
    return render(request, 'myapp/goog_count_chart.html')

def home(request):
    filter = None
    try:
        if request.user.is_superuser:
            filter = OrdersFilter(request.GET, queryset=Orders.objects.order_by('id'))
        else:
            filter = OrdersFilter(request.GET, queryset=Orders.objects.filter(owner=request.user).order_by('id'))
    except Exception as e:
        orders = None
    return render(request, 'myapp/orders_list.html', {'filter': filter})
