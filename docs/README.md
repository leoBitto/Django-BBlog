
# BBlog

BBlog is a Django app to organize articles in a website.
it uses Quill `https://quilljs.com/` and Django 4.0 . 
-----------

## Quick start


1. Add "BBlog" to your setting like this::

    ```
    INSTALLED_APPS - [
        ...
        'django-BBlog.apps.BblogConfig',
        'django_quill',
    ]
    ```

    ```
    TEMPLATES - [
        'DIRS': [   
            ...
            'BBlog/templates',
            ],
    ]
    ```

2. Include the BBlog URLconf in your project urls.py like this::

    > path('', include(('BBlog.urls', 'BBlog'), namespace="BBlog")),

3. Run ``python manage.py migrate`` to create the BBlog models.

4. Start the development server and visit http://127.0.0.1:8000/admin/
   to create the models (you'll need the Admin app enabled).

5. Visit http://127.0.0.1:8000 to see the website


-----------

# BBlog docs                       

