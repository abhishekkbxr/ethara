import os
import shutil
from pathlib import Path

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'hrms_lite.settings')

from django.core.management import call_command
from django.core.wsgi import get_wsgi_application


def _seed_vercel_sqlite() -> None:
    if not os.getenv('VERCEL'):
        return

    db_path = Path('/tmp/db.sqlite3')

    # Seed /tmp SQLite from repository db on cold start.
    if not db_path.exists() and db_path.parent == Path('/tmp'):
        source_db = Path(__file__).resolve().parent.parent / 'db.sqlite3'
        if source_db.exists():
            db_path.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(source_db, db_path)


def _migrate_vercel_sqlite() -> None:
    if os.getenv('VERCEL'):
        call_command('migrate', interactive=False, run_syncdb=True, verbosity=0)


_seed_vercel_sqlite()
app = get_wsgi_application()
_migrate_vercel_sqlite()
