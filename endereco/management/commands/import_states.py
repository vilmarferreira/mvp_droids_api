import csv
import os

from django.core.management.base import BaseCommand

# from django.db.utils import IntegrityError, DataError
from django.conf import settings

from endereco.models import Estado


class Command(BaseCommand):
    # def add_arguments(self, parser):
    #     parser.add_argument('local_type', type=str)

    def handle(self, *args, **options):
        with open(os.path.join(settings.BASE_DIR, "data", "states.csv")) as csvfile:
            reader = csv.reader(csvfile, delimiter=",", quotechar='"')
            for i, row in enumerate(reader):
                if i == 0:
                    continue
                nome, uf = row
                Estado.objects.get_or_create(
                    nome=nome,UF=uf
                )
