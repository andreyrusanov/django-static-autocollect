Sometimes with Django you need to collect static during development. It is really annoying to make it manually every time. 
There are a few ways to handle it. 
static_autocollect watches for changes in static files and runs ``collectstatic`` command for you automatically. 

Quick start
-----------
1. Install with pip:
``pip install django-static-autocollect``

2. Add "static_autocollect" to your INSTALLED_APPS:

.. code-block:: python

    INSTALLED_APPS = [
        ...
        'static_autocollect',
    ]    
    # or, since it is the app for development purposes only:   
    if DEBUG:
        INSTALLED_APPS.append('static_autocollect')

Peronally I just append it in my local settings to INSTALLED_APPS.

3. Run ``python manage.py watch_static`` to run static watcher. It will show collectstatic output, so you will be able to see what exactly(and when) has been synced.


The lib is working and quite stable already and I will update it with some tests and (perhaps) some minor features soon. 
