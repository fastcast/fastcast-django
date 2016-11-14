# Fastcast Django

## About

Django site for [GitHub](http://fastcast.nz)

## Getting Running

1. Install python, virtualenv and requirements for the ``virtualenv`` such as libpq-dev libjpeg-dev

        # If you have never used Django before this is a great tutorial to get you started https://docs.djangoproject.com/en/1.10/intro/tutorial01/
        $ sudo apt-get install python3-pip libpq-dev libjpeg-dev

2. Clone the repository and install a ``virtualenv`` and requirements:

        $ git clone https://github.com/fastcast/fastcast-django
        $ cd fastcast-django
        $ virtualenv env
        $ . env/bin/activate
        $ pip install -r requirements.txt
        $ deactivate

3. Set up and run:

        $ cp fastcast/default_settings.py fastcast/settings.py

        # Print generated secret key
        $ env/bin/python -c "from django.utils.crypto import get_random_string; chars = 'abcdefghijklmnopqrstuvwxyz0123456789%^&*(-_=+)'; secret_key = get_random_string(50, chars); print(secret_key)"

        # Edit settings.py and enter secret key and any other site-specific changes such as using PostgreSQL
        $ nano dovedale/settings.py

        # Runserver
        $ env/bin/python manage.py runserver

4. Visit http://127.0.0.1:8000/

        # You should see the basic site without any content

5. Create a user to login to admin site and add torrents

        $ env/bin/python manage.py createsuperuser
        # Visit http://127.0.0.1:8000/admin/ and login
        # Now you can add torrents and other site content :)
