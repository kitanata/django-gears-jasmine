django-gears-jasmine
====================

Run Jasmine Tests written in JavaScript or CoffeeScript w/ Django-Gears and PhantomJS


Early Project
=============

This is the first commit but this project is intended to be production
ready. It has been tested in limited capactiy if it doesn't work for you
please submit an issue and I will fix the problem as soon as possible.
Of course, I am more than open to pull requests.


Installation
============

Add ```jasmine``` to your INSTALLED_APPS *after* ```django-gears```

Add ```url(r'^jasmine/', include('jasmine.urls'))``` to your urls.py file.

Install PhantomJS from npm:
```npm install -g phantomjs```


Expectations
============

- You must put your specs inside the ```assets/js/spec``` directory
and create a manifest file for them. If you are unsure what a manifest
is then read the django-gears and Gears documentation.

- Your spec manifest file must be named ```spec.js```

- You must put your JS assets inside the ```assets/js``` directory
and create a manifest file for them.

- Your JS asset manifest file must be named ```application.js```

- You must run in DEBUG mode. (settings.DEBUG must be set to true)

- You must run your server at 127.0.0.1:8000 (which is the default)

It is a goal of this project over time to remove these Expectations
however to get things to work now you must do the above for Tests
to run.

Running Jasmine Tests
=====================

To run your tests navigate your browser to ```http://127.0.0.1:8000/jasmine```

To run tests in the command line use ```python manage.py jasmine```

LICENSE
=======

This project is released under the standard MIT License.
