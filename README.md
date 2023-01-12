# Chat App

Real Time Chat App Using Django, Channels, JavaScript, Docker, Tailwind CSS and much more..

This App is Deployed to [Render](https://render.com). <br/>
[Live Preview](https://chatapp-2.onrender.com/).

## Tech Stack:

- [WebSockets](https://developer.mozilla.org/en-US/docs/Web/API/WebSockets_API) - WebSocket is a computer communications protocol, providing full-duplex communication channels over a single TCP connection.
- [Django](https://www.djangoproject.com/) - Django makes it easier to build better web apps more quickly and with less code.
- [Django Channels](https://channels.readthedocs.io/en/stable/) - Channels is a project that takes Django and extends its abilities beyond HTTP - to handle WebSockets, chat protocols, IoT protocols, and more.
- [Vite](https://vitejs.dev/) - Next Generation Frontend Tooling.
- [Tailwind 3](https://tailwindcss.com/) - Rapidly build modern websites without ever leaving your HTML.
- [Docker](https://www.docker.com/) - Docker is a platform designed to help developers build, share, and run modern applications. We handle the tedious setup, so you can focus on the code.
- [Postgres DB](https://www.postgresql.org/) - The World's Most Advanced Open Source Relational Database.

## Getting Started

1. Clone the project and make it your own.
```bash
mkdir ~/Dev
cd ~/Dev
git clone https://github.com/Arvind-4/Chatapp.git
cd Chatapp
```

2. Create virtual environment and activate it.

```bash
python3.9 -m venv .
source bin/activate
```
Use `.\venv\Scripts\activate` if on **Windows.**

3. Install requirements
```bash
$(Chatapp) python -m pip install pip --upgrade
$(Chatapp) python -m pip install -r requirements.txt
```

4. Open VSCode
```bash
code .
```

5. Create `.env` file:

Add Your Credentials `.env` from `.env.sample`:
```
DJANGO_PG_PASSWORD=postgres
DJANGO_PG_HOST=localhost
DJANGO_PG_USER=postgres
DJANGO_PG_DATABASE=postgres
DJANGO_PG_PORT=5432

DJANGO_REDIS_URL=redis://localhost:6379

DJANGO_SUPERUSER_EMAIL=arvind@host.com
DJANGO_SUPERUSER_USERNAME=admin
DJANGO_SUPERUSER_PASSWORD=bad-password

DJANGO_SECRET_KEY=
DJANGO_ADMIN_URL=admin/
DJANGO_DEBUG=1
DJANGO_ALLOWED_HOSTS=*

DJANGO_LIVE=0

PYTHON_VERSION=3.9.14
```
Replace your `SECRET_KEY` with a new one using the code Below.

```bash
python -c 'from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())'
```

6. Build and Start the Docker File:

Below will start a Docker Instance on your local machine to match the `.env` from the previous step.
```bash
docker build -t chatapp:v1 .
```
Start the Docker Build Image:
```bash
docker run -it -p 8000:8000 chatapp:v1
```

7. Run Django Commands & Migrations and Create Superuser
```bash
cd ~/Dev/Chatapp
source bin/activate
$(Chatapp) python manage.py makemigrations
$(Chatapp) python manage.py migrate
$(Chatapp) python manage.py createsuperuser
```

Run the server:
```bash
$(Chatapp) python manage.py runserver
```

8. Install & Build the Frontend.

Install the Required Dependencies
```bash
npm run i
```
Build the Frontend for Production
```bash
npm run production
```

9. Celebrate!

## Deploy to Render:
Click the Button to Deploy to [Render](https://render.com/).

[![Deploy to Render](https://render.com/images/deploy-to-render-button.svg)](https://render.com/deploy?repo=https://github.com/Arvind-4/Chatapp)

## Change Log:
[Change Log](https://github.com/Arvind-4/Chatapp/commits/main).

## License:
This Project is [MIT LICENSE](https://github.com/Arvind-4/Chatapp/blob/main/LICENSE).
