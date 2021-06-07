from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import make_password
from django.core.management.base import BaseCommand

from faker import Faker

UserModel = get_user_model()


class Command(BaseCommand):
    help = 'Создание случайного пользователя c username, email и password'  # noqa A003

    def add_arguments(self, parser):
        parser.add_argument('total', type=int, choices=range(1, 11), help='Количество создаваемых пользователей')

    def handle(self, *args, **kwargs):
        fake = Faker()
        total = kwargs['total']
        objs = [
            UserModel(
                username=fake.name(),
                email=fake.email(),
                password=make_password('password')
            )
            for _ in range(total)
        ]

        UserModel.objects.bulk_create(objs)
        self.stdout.write(self.style.SUCCESS('Успешно'))
