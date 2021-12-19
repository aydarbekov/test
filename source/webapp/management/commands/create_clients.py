from django.core.management.base import BaseCommand

from webapp.models import Client


class Command(BaseCommand):
    help = 'Add default clients' # Описание команды

    def handle(self, *args, **kwargs):
        for i in range(30000):
            client = Client()
            client.name = f'Имя №{i+1}'

            client.save()

        print('All default cats updated. Have a nice day!')
