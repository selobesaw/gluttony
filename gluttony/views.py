from django.views.generic import ListView

from gluttony.models import Dish


class DishLishView(ListView):
    model = Dish
    paginate_by = 9

    def get_queryset(self):

        return super().get_queryset()
