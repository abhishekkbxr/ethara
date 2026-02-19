import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'hrms_lite.settings')

from django.core.management import call_command
from django.core.wsgi import get_wsgi_application

app = get_wsgi_application()

# Optional for SQLite on serverless: ensure tables exist on cold start.
if os.getenv('VERCEL') and os.getenv('RUN_MIGRATIONS', '1') == '1':
    try:
        call_command('migrate', interactive=False, run_syncdb=True, verbosity=0)
    except Exception:
        # Avoid crashing the import path; API responses will surface DB errors if migration fails.
        pass
