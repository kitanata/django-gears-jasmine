import os
import subprocess

from django.core.management.base import BaseCommand, CommandError
from django.conf import settings

class Command(BaseCommand):
    help = 'Run Django Jasmine Tests'

    def __init__(self, *args, **kwargs):
        super(Command, self).__init__(*args, **kwargs)

        self.js_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', 'static/js'))
        self.runner = os.path.join(self.js_dir, 'run_jasmine_test.coffee')


    def handle(self, *args, **options):
        if settings.DEBUG:
            result = subprocess.call(['phantomjs', self.runner, "http://127.0.0.1:8000/jasmine/ci"])
        else:
            return "DEBUG must be set True and server must be running in 127.0.0.1:8000"

        return "DONE!"
