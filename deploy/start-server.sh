#!/usr/bin/env bash

chown -R www-data:www-data /fixes_web

python -m pip install -U pip
python -m pip install -r requirements.txt

# replace with these following code to use your own index url
# python -m pip install -U pip -i https://pypi.douban.com/simple/
# python -m pip install -r requirements.txt -i https://pypi.douban.com/simple/

python manage.py migrate
python manage.py collectstatic --noinput
if [ -n "$DJANGO_SUPERUSER_USERNAME" ] && [ -n "$DJANGO_SUPERUSER_PASSWORD" ] ; then
    (python manage.py createsuperuser --no-input --email test@fixes.com)
fi

python manage.py runserver 0.0.0.0:8000
