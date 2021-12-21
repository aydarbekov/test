import random

import pytz
from django.core.management.base import BaseCommand

from webapp.models import Client, Department


class Command(BaseCommand):
    help = 'Add default clients' # Описание команды

    def handle(self, *args, **kwargs):
        sex = ['male', 'female', 'unknown']
        TIMEZONES = tuple(zip(pytz.all_timezones, pytz.all_timezones))

        for i in range(30000):
            client = Client()
            client.identity_number = f'{i+1}'
            client.mobile_phone = '+9967081' + '0' * (7 - len(str(i))) + str(i)
            print(client.mobile_phone)
            client.last_name = f'Фамилия №{i+1}'
            client.first_name = f'Имя №2{i+1}'
            client.username = client.first_name
            client.middle_name = f'Отчество №{i+1}'
            client.client_type = random.choice(sex)
            client.identity_number = f'{i+1}'
            client.timezone = random.choice(TIMEZONES)
            parent = random.choice(Department.objects.all())
            client.save()
            client.departments = parent
            client.save()
        print('All default clients updated. Have a nice day!')
