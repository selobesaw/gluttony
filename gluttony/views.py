from django.db.models import Sum
from django.shortcuts import redirect
from django.views.generic import ListView

from gluttony.models import Dish, Allergen


class DishLishView(ListView):
    model = Dish
    ordering = ('category', 'name')

    def post(self, request):
        request.session['dishes'] = request.POST.getlist('dish')
        return redirect('order')


class OrderView(ListView):
    template_name = 'gluttony/order.html'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        queryset = kwargs['object_list'] if 'object_list' in kwargs else self.object_list
        context.update(queryset.aggregate(Sum('energy'), Sum('price')))
        context['allergens'] = Allergen.objects.filter(dish__in=queryset).distinct()
        return context

    def get_queryset(self):
        return Dish.objects.filter(pk__in=self.request.session['dishes'])
