from django.core.management import BaseCommand
from django.db import connection

from main.models import Product
from django.utils import timezone

class Command(BaseCommand):
    def handle(self, *args, **options):
        Product.objects.all().delete()

        self.stdout.write(self.style.SUCCESS('Resetting autoincrement ID...'))
        with connection.cursor() as cursor:
            cursor.execute("ALTER SEQUENCE main_product_id_seq RESTART WITH 1;")

        products_list = [
            {'name': 'neMoloko', 'description': 'Вкусно и полезно', 'category': 'Молочные продукты', 'price_per_unit': 60, 'creation_date': timezone.now(), 'last_modified_date': timezone.now()},
            {'name': 'Йогурт', 'description': 'Очень вкусно', 'category': 'Молочные продукты', 'price_per_unit': 60, 'creation_date': timezone.now(), 'last_modified_date': timezone.now()},
            {'name': 'Творог', 'description': 'Невероятно delicious', 'category': 'Молочные продукты', 'price_per_unit': 60, 'creation_date': timezone.now(), 'last_modified_date': timezone.now()},
            {'name': 'Молоко', 'description': 'Вкусненько', 'category': 'Молочные продукты', 'price_per_unit': 60, 'creation_date': timezone.now(), 'last_modified_date': timezone.now()},
            {'name': 'Сосиски', 'description': 'Не полезно', 'category': 'Мясные продукты', 'price_per_unit': 60, 'creation_date': timezone.now(), 'last_modified_date': timezone.now()},
            {'name': 'Котлетки', 'description': 'Много консервантов', 'category': 'Мясные продукты', 'price_per_unit': 60, 'creation_date': timezone.now(), 'last_modified_date': timezone.now()},
            {'name': 'Веганские котлетки', 'description': 'Более менее полезно', 'category': 'Мясные продукты', 'price_per_unit': 60, 'creation_date': timezone.now(), 'last_modified_date': timezone.now()},
            {'name': 'Тортик', 'description': 'Delicious', 'category': 'Sweets','price_per_unit': 60, 'creation_date': timezone.now(), 'last_modified_date': timezone.now()}
        ]


        # for product_item in products_list:
        #     Product.objects.create(**product_item)

        products_for_create = [Product(**product_item) for product_item in products_list]


        Product.objects.bulk_create(products_for_create)

