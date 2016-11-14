# Fastcast Django

## About

Django site for [Fastcast](http://fastcast.nz)

You can still use the static [Fastcast](https://github.com/fastcast/fastcast) repository

## Getting Running

#### If you have never used Django before this is a great tutorial to get you started https://docs.djangoproject.com/en/1.10/intro/tutorial01/

1. Install python, virtualenv and requirements for the ``virtualenv`` such as libpq-dev libjpeg-dev

        $ sudo apt-get install python3-pip libpq-dev libjpeg-dev
        $ pip install virtualenv

2. Clone the repository and install the ``virtualenv`` and requirements:

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

        # Edit settings.py and enter secret key and make any other site-specific changes such as configuring PostgreSQL
        $ nano dovedale/settings.py

        # Runserver
        $ env/bin/python manage.py runserver

4. Visit http://127.0.0.1:8000/

        # You should see the basic site without any content

5. Create a user to login to admin site

        $ env/bin/python manage.py createsuperuser
       
6. Visit http://127.0.0.1:8000/admin/ and login
  
        # Now you can add torrents and other site content :)
