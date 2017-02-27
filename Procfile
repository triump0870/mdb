web: python src/manage.py collectstatic --noinput
web: gunicorn --chdir src/ mdb.wsgi --preload
