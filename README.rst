Static autocollect watches for changes in static files and runs `collectstatic` command for you.

Quick start
-----------

1. Add "static_autocollect" to your INSTALLED_APPS setting like this::

    INSTALLED_APPS = [
        ...
        'static_autocollect',
    ]

3. Run `python manage.py static_watch` to run static watcher.
