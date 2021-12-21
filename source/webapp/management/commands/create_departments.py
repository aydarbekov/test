import random

import pytz
from django.core.management.base import BaseCommand

from webapp.models import Department


class Command(BaseCommand):
    help = 'Add default departments' # Описание команды

    def handle(self, *args, **kwargs):

        for i in range(500):
            department = Department()
            department.identity_number = f'{i+1}'
            department.name = f'Департамент №{i+1}'
            if_parent = random.choice([0, 1])
            if if_parent == 1:
                while True:
                    parent = random.choice(Department.objects.all())
                    if parent.get_descendant_count() < 6:
                        department.parent = parent
                        break
            department.save()
        print('All default clients updated. Have a nice day!')
