from rest_framework import serializers

from gluttony.api_fields import Base64ImageField
from gluttony.models import Dish


class DishSerializer(serializers.ModelSerializer):
    image = Base64ImageField(label='Изображение', required=False, help_text='Можно использовать Base64')

    class Meta:
        model = Dish
        exclude = ('allergens',)
