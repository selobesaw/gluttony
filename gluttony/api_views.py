from django.conf import settings
from rest_framework import generics, authentication, exceptions

from gluttony.models import Dish
from gluttony.serializers import DishSerializer


class DishListCreateAPIView(generics.ListCreateAPIView):
    serializer_class = DishSerializer
    queryset = Dish.objects

    def post(self, request, *args, **kwargs):
        header = authentication.get_authorization_header(request).decode(errors='ignore').split()
        if header and len(header) == 2 and header[0].lower() == 'token' and header[1] == settings.API_TOKEN:
            return super().post(request, *args, **kwargs)
        raise exceptions.AuthenticationFailed
