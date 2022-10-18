from django.core.management import BaseCommand

from core.models import IncidentName


class Command(BaseCommand):

    def handle(self, *args, **options):
        for i in range(10):
            IncidentName.objects.get_or_create(name=f"name{i}")
