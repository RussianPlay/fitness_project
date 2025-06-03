from django.db import models
from django.contrib.auth.models import User
import datetime
import random
# Create your models here.
class Category(models.Model):
    en_rus_catalog = {
    "velosport": "Велоспорт",
    "samokaty": "Самокаты",
    "trenazhyory-i-fitnes": "Тренажеры и фитнес",
    "futbol": "Футбол",
    "beg": "Бег",
    "vodnyy_turizm": "Водный Туризм",
    "roliki": "Ролики",
    "edinoborstva": "Единоборства",
    "yoga": "Йога",
    "fishing": "Рыбалка",
    "plavanie": "Плавание",
    "turizm": "Туризм",
    "gornyy_turizm": "Треккинг",
    "alpinizm": "Альпинизм",
    "kemping": "Кемпинг",
    "tennis": "Теннис",
    "skeytbording": "Мини-круизеры",
    "beg_po_bezdorozhyu": "Трейлраннинг",
    "begovye_lyzhi": "Беговые лыжи",
    "gornye_lyzhi": "Горные лыжи",
    "snoubording": "Сноубординг",
    "konki": "Коньки",
    "sanki_i_snegokaty": "Санки и Тюбинги",
    "khokkey": "Хоккей",
    "aktivnaya-zima": "Активная зима",
    "plyazh": "Пляж",
}

    name = models.CharField(max_length=50)
    @staticmethod
    def get_all_categories():
        return Category.objects.all()

    def __str__(self):
        return self.name
    
    def get_translated_name(self):
        return Category.en_rus_catalog.get(self.name, self.name)



class Products(models.Model):
    RATING_CHOICES = [
        (0, '0'),
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5'),
    ]
    name = models.CharField(max_length=60)
    price= models.IntegerField(default=0)
    category= models.ForeignKey(Category,on_delete=models.CASCADE,default=1 )
    description= models.CharField(max_length=250, default='', blank=True, null= True)
    company_name = models.CharField(max_length=60, default='GOD')
    rating = models.IntegerField(choices=RATING_CHOICES, default=0)
    image= models.URLField(max_length=200,  # Максимальная длина URL
        blank=True,      # Разрешить пустое значение 
        null=True,       # Разрешить NULL в БД 
        default='',      # Значение по умолчанию 
        verbose_name='Ссылка на сайт')  # Человекочитаемое название
    
    @staticmethod
    def get_products_by_id(ids):
        return Products.objects.filter(id__in=ids)
    @staticmethod
    def get_all_products():
        return Products.objects.all()

    @staticmethod
    def get_all_products_by_categoryname(category_name):
        if category_name is None:
           return Products.objects.all()
        try:
            category = Category.objects.get(name__iexact=category_name)
            products = Products.objects.filter(category=category)
        except Category.DoesNotExist:
            ## или лучше пустое
            products = Products.objects.all()
        return products
        
    @staticmethod
    def get_size():
        return Products.objects.count()
    
    @staticmethod
    def get_recommended_products(max_count = 4):
        total = min(max_count, Products.get_size())
        return Products.objects.order_by('?')[:total]
    
    @staticmethod
    def get_products_page(page_number=1, page_size=20, sort_command=None):
        # page_number - номер страницы (начиная с 1)
        # page_size - количество продуктов на странице (20 по умолчанию)
        if not sort_command:
            all_products = Products.objects.all().order_by('id')
        else:
            all_products = Products.get_all_products_by_categoryname(sort_command).order_by('id')
        start_index = (page_number - 1) * page_size
        end_index = min(len(all_products), start_index + page_size)
        # Получаем 20 продуктов для i-той страницы
        products_page = all_products[start_index:end_index]
        return products_page


class Order(models.Model):
    product = models.ForeignKey(Products,
                                on_delete=models.CASCADE)
    user = models.ForeignKey(User,
                                 on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    price = models.IntegerField()
    address = models.CharField(max_length=50, default='', blank=True)
    phone = models.CharField(max_length=50, default='', blank=True)
    date = models.DateField(default=datetime.datetime.today)
    status = models.BooleanField(default=False)

    def placeOrder(self):
        self.save()

    @staticmethod
    def get_orders_by_user(user_id):
        return Order.objects.filter(customer=user_id).order_by('-date')
