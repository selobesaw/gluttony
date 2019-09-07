from django.db import models


class Allergen(models.Model):
    name = models.CharField('Название', max_length=50)

    class Meta:
        verbose_name = 'аллерген'
        verbose_name_plural = 'аллергены'

    def __str__(self):
        return self.name


class Dish(models.Model):
    allergens = models.ManyToManyField(Allergen, verbose_name='Аллергены', blank=True)
    category = models.CharField('Категория', max_length=50)
    energy = models.IntegerField('Энергетическая ценность, ккал')
    image = models.ImageField('Изображение', upload_to='images', blank=True)
    name = models.CharField('Название', max_length=50)
    price = models.DecimalField('Стоимость за порцию, ₽', max_digits=9, decimal_places=2)

    class Meta:
        verbose_name = 'блюдо'
        verbose_name_plural = 'блюда'

    def __str__(self):
        return self.name
