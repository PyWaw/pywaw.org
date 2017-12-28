../containers/wait-for-it.sh -t 60 db:5432
python manage.py migrate --noinput
python manage.py collectstatic --noinput
uwsgi --socket :8000 --module pywaw.wsgi --processes 4 --threads 2