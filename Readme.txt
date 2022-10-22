python3 -m pip install django
django-admin startproject admin
cd admin
python3 manage.py runserver

chrome: http://127.0.0.1:8000

## install docker desktop



Repo: https://github.com/antoniopapa/django-admin

## if you used plugin to docker, instead of docker-compose package - https://www.digitalocean.com/community/tutorials/how-to-install-and-use-docker-compose-on-ubuntu-22-04
## then use "docker compose" instead of "docker-compose"
docker-compose up
docker-compose exec admin_api sh
# python manage.py startapp users
# python manage.py migrate
# python manage.py createsuperuser --email a@a.com

chrome: http://127.0.0.1:8000/admin 
