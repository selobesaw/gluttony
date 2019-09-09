from django.db.models import Sum
from django.shortcuts import render
from django.views.generic import ListView

from gluttony.models import Allergen, Dish


class DishLishView(ListView):
    model = Dish
    ordering = ('category', 'name')


class OrderView(ListView):
    template_name = 'gluttony/order.html'

    def get_context_data(self, *args, **kwargs):
        queryset = kwargs['object_list'] if 'object_list' in kwargs and kwargs['object_list'] is not None else self.object_list

        context = super().get_context_data(*args, **kwargs)
        context.update(queryset.aggregate(Sum('energy'), Sum('price')))
        context['allergens'] = Allergen.objects.filter(dish__in=queryset).distinct()

        return context

    def get_queryset(self):
        return Dish.objects.filter(pk__in=self.request.POST.getlist('dish'))

    # знаю, что выглядит шаблонно, но не знаю, где реализация из встроенных миксинов
    def post(self, request):
        return render(request, self.template_name, self.get_context_data(object_list=self.get_queryset()))
