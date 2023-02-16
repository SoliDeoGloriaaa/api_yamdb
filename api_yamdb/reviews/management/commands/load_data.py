import csv

from django.conf import settings
from django.core.management import BaseCommand

from api_yamdb.reviews.models import (
    User, Category, Genre, Title, Review, Comment, GenreTitle
)


TABLES = {
    User: 'users.csv',
    Category: 'category.csv',
    Genre: 'genre.csv',
    GenreTitle: 'genre_title.csv',
    Title: 'titles.csv',
    Review: 'review.csv',
    Comment: 'comments.csv',
}


class Command(BaseCommand):

    def handle(self, *args, **kwargs):
        for model, base in TABLES.items():
            with open(
                f'{settings.BASE_DIR}/static/data/{base}',
                'r',
                encoding='utf-8'
            ) as csv_file:
                reader = csv.DictReader(csv_file)
                model.objects.bulk_create(
                    model(**data) for data in reader)
        self.stdout.write(self.style.SUCCESS('Все данные загружены'))
