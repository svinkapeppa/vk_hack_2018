import os
import sys

from django.core.wsgi import get_wsgi_application

app_path = os.path.dirname(os.path.abspath(__file__)).replace('/config', '')
sys.path.append(os.path.join(app_path, 'app'))

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings.settings")

application = get_wsgi_application()
