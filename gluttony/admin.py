from django.contrib import admin

from gluttony.models import Allergen, Category, Dish


class DishAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'price')
    list_filter = ('category', 'allergens')


admin.site.register(Allergen)
admin.site.register(Category)
admin.site.register(Dish, DishAdmin)
