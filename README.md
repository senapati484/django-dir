# Django Example Project

This repository contains a small example Django project named `myproject` with a single app `myapp`. It's a minimal starter demonstrating templates, views, forms, and basic project structure.

## Project structure

- myproject/                 - Django project package
  - myproject/               - project settings, URLs, ASGI/WSGI
    - settings.py
    - urls.py
    - asgi.py
    - wsgi.py
  - myapp/                   - single Django app
    - templates/             - HTML templates used by the app
      - home.html
      - about.html
      - form.html
      - shoping.html
    - views.py
    - models.py
    - forms.py
    - admin.py
    - apps.py
    - tests.py
    - migrations/
- manage.py                  - Django management script
- db.sqlite3                 - SQLite database (example/dev)

## Requirements

- Python 3.8+ (or compatible)
- Django (the project was developed with Django 3.x or 4.x — install latest stable)

Install dependencies in a virtual environment:

python -m venv .venv
source .venv/bin/activate
pip install --upgrade pip
pip install django

If you have a requirements.txt add it and run:

pip install -r requirements.txt

## Setup & Run (development)

1. Apply migrations:

python manage.py migrate

2. (Optional) Create a superuser for admin access:

python manage.py createsuperuser

3. Run development server:

python manage.py runserver

Visit http://127.0.0.1:8000/ in your browser.

## What this project demonstrates

- Simple multi-template setup in a Django app (`home`, `about`, `form`, `shoping`).
- Basic view functions defined in `myapp/views.py` rendering templates.
- A place for forms in `myapp/forms.py` and models in `myapp/models.py` for future extension.

## Common tasks

- Add a new view:
  - Edit myapp/views.py and create a template under myapp/templates/.
  - Add a URL pattern in myproject/urls.py or a dedicated myapp/urls.py and include it.

- Add a model:
  - Define model in myapp/models.py, run `python manage.py makemigrations` and `python manage.py migrate`.

- Static files:
  - For production, configure STATIC_ROOT and collect static with `python manage.py collectstatic`.

## Notes

- The repository includes an example SQLite database `db.sqlite3`. Remove or replace it for production use.
- Update `myproject/settings.py` to set SECRET_KEY, DEBUG, ALLOWED_HOSTS, database, and other production settings before deploying.

## Helpful commands

- Run tests: python manage.py test
- Create migrations: python manage.py makemigrations
- Apply migrations: python manage.py migrate
- Create superuser: python manage.py createsuperuser

## License

This project is provided as-is for learning and reference. Add a LICENSE file if you intend to publish or distribute it.

