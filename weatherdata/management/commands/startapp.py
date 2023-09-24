from django.core.management.base import BaseCommand
import subprocess
import os

class Command(BaseCommand):
    help = 'Start the Django app along with the consumers script'

    def handle(self, *args, **kwargs):

        subprocess.Popen(["python", os.path.join(os.path.dirname(__file__), "../../consumers.py")])

        os.system('python manage.py runserver')
