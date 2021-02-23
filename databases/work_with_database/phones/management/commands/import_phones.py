import csv

from django.core.management.base import BaseCommand
from phones.models import Phone
from django.utils.text import slugify


class Command(BaseCommand):
    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        with open('phones.csv', 'r') as csvfile:

            phone_reader = csv.reader(csvfile, delimiter=';')
            # пропускаем заголовок
            next(phone_reader)

            for line in phone_reader:
                new_phone = Phone()
                new_phone.id = line[0]
                new_phone.name = line[1]
                new_phone.image = line[2]
                new_phone.price = line[3]
                new_phone.release_date = line[4]
                new_phone.lte_exists = line[5]
                new_phone.slug = slugify(new_phone.name)
                new_phone.save()
