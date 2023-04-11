
# BBlog

BBlog is a Django app to organize articles in a website.
it uses Quill `https://quilljs.com/` and Django 4.2 . 
-----------

## Quick start
0. after cloning the repo inside the Django project rename the folder containing 
    this app eliminating the name django_

1. Add "BBlog" to your setting like this::

    ```
    INSTALLED_APPS - [
        ...
        'BBlog.apps.BblogConfig',
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
you may want to add some url path inside the ''

    > path('', include(('BBlog.urls', 'BBlog'), namespace="BBlog")),

3. Run ``python manage.py migrate BBlog`` to create the BBlog models.

4. the base.html template need a footer and a navbar that can be integrated
    from other apps

4. Start the development server and visit http://127.0.0.1:8000/admin/
   to create the models (you'll need the Admin app enabled).

5. Visit http://127.0.0.1:8000 to see the website


-----------

# BBlog docs                       
if you want to use the article links outside the app you need to use the namespace.
it is always a good idea when having many apps inside a Django project to use the namespace.
for example:

    > <a href="{% url 'BBlog:article' slug=article.slug  %}"</a>

