release: python manage.py migrate --noinput

web: daphne -b 0.0.0.0 app:app 

worker: python manage.py rqworker default