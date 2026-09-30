# Class -11

- [Class -11](#class--11)
  - [Project Setup](#project-setup)
  - [Django File Structure](#django-file-structure)
  - [`home_page` View — Hello, World](#home_page-view--hello-world)
  - [`home_page` URL — First Attempt](#home_page-url--first-attempt)
  - [`home_page` URL — Fixed & Root `/` Added](#home_page-url--fixed--root--added)
  - [`about_page` View & URL](#about_page-view--url)
  - [Create Superuser](#create-superuser)
  - [Database Migrations](#database-migrations)
  - [Project Structure](#project-structure)
  - [Final Output](#final-output)

This README follows the actual **commit history** of the project — every section below matches one real commit, in the same order they were built. This is an early/basic Django class exercise, so `views.py` and `urls.py` live directly inside the project package (`class_02/class_02/`) rather than in a separate app.

## Project Setup

- Create and activate a virtual environment

  ```sh
  python -m venv venv
  venv\Scripts\activate      # Windows
  source venv/bin/activate   # Linux/Mac
  ```

- Install Django

  ```sh
  pip install django
  ```

- Create the project

  ```sh
  django-admin startproject class_02
  cd class_02
  ```

- Run the development server to confirm the base install works

  ```sh
  py manage.py runserver
  ```

---
[⬆️ Go to Context](#class--11)

## Django File Structure

- At this point, no app was created yet — instead, two new files are added directly inside the project's inner folder, next to `settings.py` and the default `urls.py`:

  ```txt
  📁 class_02
  └── 📁 class_02
      ├── 🐍 settings.py
      ├── 🐍 urls.py
      ├── 🐍 views.py     # NEW
      └── 🐍 wsgi.py
  ```

- [note.html](./note.html) is a plain HTML file used as running class notes (not part of the app itself) — it lists the exact terminal commands covered in this class, in order:

  ```txt
  python manage.py createsuperuser
  python manage.py makemigrations
  python manage.py migrate
  ```

---
[⬆️ Go to Context](#class--11)

## `home_page` View — Hello, World

- A `views.py` file is created directly inside the project package, with a single view function returning a plain text response

  ```py
  from django.http import HttpResponse

  def home_page(request):
      return HttpResponse('Hello, World')
  ```

- `HttpResponse(...)` — the simplest possible Django response, returns raw text directly to the browser with no template involved. This is the starting point before templates (`render()`) are introduced in later classes

---
[⬆️ Go to Context](#class--11)

## `home_page` URL — First Attempt

- A route for `home_page` is added in [urls.py](./class_02/class_02/urls.py), but at first **without** the trailing slash convention Django expects

  ```py
  from .views import home_page

  urlpatterns = [
      path('admin/', admin.site.urls),
      path('home', home_page, name='home'),   # missing trailing slash
  ]
  ```

> [!NOTE]
> Django convention is to end URL patterns with a `/` (e.g. `'home/'`). Without it, visiting `/home` still mostly works, but Django's `APPEND_SLASH` behavior and URL matching can behave inconsistently — this is exactly what gets corrected in the very next commit.

---
[⬆️ Go to Context](#class--11)

## `home_page` URL — Fixed & Root `/` Added

- The trailing slash is fixed, and a route for the root URL (`/`) is added — this is the version that ships in the final code

  ```py
  from django.contrib import admin
  from django.urls import path
  from .views import home_page, about_page

  urlpatterns = [
      path('admin/', admin.site.urls),
      path('home/', home_page, name='home'),
      path('about/', about_page, name='about'),
  ]
  ```

- `path('home/', home_page, name='home')` — the trailing `/` now follows Django's convention
- `name='home'` — gives the URL a reusable name, so it can be referenced later in templates with `{% url 'home' %}` instead of hardcoding `/home/`

---
[⬆️ Go to Context](#class--11)

## `about_page` View & URL

- A second view is added the same way, in [views.py](./class_02/class_02/views.py)

  ```py
  def about_page(request):
      return HttpResponse('About page')
  ```

- And wired up in [urls.py](./class_02/class_02/urls.py)

  ```py
  path('about/', about_page, name='about'),
  ```

- Same pattern as `home_page`: plain text response, no template — reinforcing the view → URL connection before templates are introduced

---
[⬆️ Go to Context](#class--11)

## Create Superuser

- To access Django's built-in admin panel, an admin account is created

  ```sh
  py manage.py createsuperuser
  ```

> [!IMPORTANT]
> As [note.html](./note.html) points out, running this command **before** the database has been migrated throws an error — Django needs the `auth_user` table to exist first. That's exactly why the next two commits (migrations) come right after this one, followed by a final, successful superuser creation.

---
[⬆️ Go to Context](#class--11)

## Database Migrations

- Since a fresh Django project's default tables (`auth`, `admin`, `sessions`, etc.) hadn't been created in the database yet, migrations are generated and applied

  ```sh
  py manage.py makemigrations
  py manage.py migrate
  ```

- `makemigrations` — scans installed apps for model changes and writes migration files (mostly a no-op here, since no custom models exist yet — this mainly picks up Django's own built-in apps)
- `migrate` — actually runs those migrations against `db.sqlite3`, creating the necessary tables

- With the database ready, `createsuperuser` is run again — this time successfully

  ```sh
  py manage.py createsuperuser
  ```

---
[⬆️ Go to Context](#class--11)

## Project Structure

```txt
class_02/
├── class_02/
│   ├── settings.py
│   ├── urls.py           # home/, about/, admin/ routes
│   ├── views.py            # home_page, about_page
│   ├── asgi.py
│   └── wsgi.py
├── db.sqlite3
├── manage.py
└── note.html               # class notes: superuser + migration commands
```

---
[⬆️ Go to Context](#class--11)

## Final Output

- `http://127.0.0.1:8000/home/` → `Hello, World`
- `http://127.0.0.1:8000/about/` → `About page`
- `http://127.0.0.1:8000/admin/` → Django admin login (usable after superuser creation + migration)

**Flow:** Project setup → plain-text views (`home_page`, `about_page`) → URL routing (fixing the trailing-slash mistake along the way) → migrate the database → create a working superuser

---
[⬆️ Go to Context](#class--11)
