import random

import pytz
from django.core.management.base import BaseCommand

from webapp.models import Client, Department, LegalEntity


class Command(BaseCommand):
    help = 'Add default legalentities' # Описание команды

    def handle(self, *args, **kwargs):
        for i in range(200):
            legal = LegalEntity()
            legal.identity_number = f'{i+1}'
            legal.full_name = f'Название №{i+1}'
            legal.short_name = f'Сокр название №{i+1}'
            legal.inn = f'Инн №{i+1}'
            legal.kpp = f'КПП №{i+1}'
            legal.save()
        print('All default clients updated. Have a nice day!')
