from django.contrib.auth.models import User
from django.db import models


class Watch(models.Model):
    name = models.CharField(max_length=500, verbose_name='Имя бренда')
    brand = models.CharField(max_length=500, verbose_name='Бренд')
    made_city = models.CharField(max_length=150, verbose_name='Произведено:')
    differences = models.TextField(max_length=500, verbose_name='Отличительные черты')
    description = models.TextField(verbose_name="Описание:")
    price = models.IntegerField(default=0, verbose_name="Цена:")
    cat_id = models.ForeignKey("Category",on_delete=models.CASCADE, verbose_name="Категория:")
    user = models.ForeignKey( User,verbose_name='Пользователь',  on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Category(models.Model):
    category = models.CharField(max_length=100)

    def __str__(self):
        return self.category






