web: gunicorn redinstagram.wsgi -c etc/config/gunicorn.py
worker: celery --workdir=redinstagram/ --app=redinstagram.celery:app worker
beat: celery --workdir=redinstagram/ --app=redinstagram.celery:app beat
flower: celery --workdir=redinstagram/ --app=redinstagram.celery:app flower
