==========
MyUsers
==========

This a little Django application that implements a custom user
following the pattern described by Will Vincent
(`https://wsvincent.com/django-custom-user-model-tutorial/`)

Unlike earlier apps (simple_auth), this application strives to use
only base django functionality, without any additional, external
dependencies.

The application also includes several templates and forms that use
semantic-ui for logging in and out, user registration, password
management.  They can be found in ~/myuser/templates directory.

To use the application, include 'myuser' in the list of installed
applications of a *new* django project *before* your first migration,
and add this line somewhere in your settings file:

AUTH_USER_MODEL = 'myusers.CustomUser'


Additionally, add these lines to the base url.py file:

    path('users/', include('myusers.urls')),
    path('users/', include('django.contrib.auth.urls')),

Run your initial migration as usual, and run the development server.
If you naviate to `localhost:8000//users/login` you should see the
new, semantic login form that uses e-mail by default.


Optional Settings
----------------

Depending on how your application is set up, you may also want to add
these variables to your settings.py file:

LOGIN_URL = 'login'
LOGIN_REDIRECT_URL = 'home'
LOGOUT_REDIRECT_URL = 'home'

EMAIL_BACKEND = 'django.core.mail.backends.filebased.EmailBackend'
EMAIL_FILE_PATH = os.path.join(BASE_DIR, 'sent_mails')


Templates
------------

There are several templates included in this application. The
templates have been styled with semantic-ui for a clean, uncluttered
appearance.  they can be found in the root ~/templates directory.  The
base template includes the follow blocks:

+ title
+ extra_head
+ content
+ extra_scripts


Tests
--------


To run the tests, simply run the command:

    > py.test
