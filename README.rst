django-webpacker's documentation:
=====================================

.. image:: https://readthedocs.org/projects/django-webpacker/badge/?version=latest
   :target: http://django-webpacker.readthedocs.io/en/latest/?badge=latest
   :alt: Documentation Status

.. image:: https://coveralls.io/repos/github/MicroPyramid/django-webpacker/badge.svg?branch=master
   :target: https://coveralls.io/github/MicroPyramid/django-webpacker?branch=master

.. image:: https://travis-ci.org/MicroPyramid/django-webpacker.svg?branch=master
    :target: https://travis-ci.org/MicroPyramid/django-webpacker

.. image:: https://landscape.io/github/MicroPyramid/django-webpacker/master/landscape.svg?style=flat
   :target: https://landscape.io/github/MicroPyramid/django-webpacker/master
   :alt: Code Health

.. image:: https://img.shields.io/github/license/micropyramid/django-webpacker.svg
    :target: https://pypi.python.org/pypi/django-webpacker/


Introduction:
=============

django-webpacker is a django compressor tool which bundles css, js files to a single css, js file with webpack and updates your html files with respective css, js file path.

It supports django-storages to load compressed files from AWS S3.

Source Code is available in Micropyramid Repository(https://github.com/MicroPyramid/django-webpacker).


Installation Procedure
======================

1. Install django-web-packer using the following command::

    pip install django-webpacker

    		(or)

    git clone git://github.com/micropyramid/django-webpacker.git

    cd django-webpacker

    python setup.py install

2. Add app name in project settings.py file::

    INSTALLED_APPS = [
       '..................',
       'django-webpacker',
       '..................'
    ]

3. Run npm init to intialize npm modules and it will create 'package.json' file which will contain package information. Update file with following dependencies::

     "devDependencies": {
        "babel": "^6.23.0",
        "babel-core": "^6.24.0",
        "babel-loader": "^6.4.1",
        "css-loader": "^0.28.0",
        "extract-text-webpack-plugin": "^2.1.0",
        "file-loader": "^0.11.1",
        "html-webpack-inline-source-plugin": "0.0.7",
        "html-webpack-plugin": "^2.28.0",
        "image-webpack-loader": "^3.3.0",
        "less-loader": "^4.0.3",
        "node-sass": "^4.5.2",
        "react": "^15.4.2",
        "react-hot-loader": "^1.3.1",
        "sass-loader": "^6.0.3",
        "script-loader": "^0.7.0",
        "style-loader": "^0.16.1",
        "webpack": "^2.3.3",
        "webpack-bundle-tracker": "^0.2.0",
        "webpack-dev-server": "^2.4.2"
      },
      "dependencies": {
        "imports-loader": "^0.7.1",
        "jquery": "^3.2.1"
      }

4. Run npm install to install all package dependencies.

    npm install

5. Updates Your html file with the following script, link stylesheet tags.

    <link rel="stylesheet" type="text/css" href="" id="packer_css"/>

    <script id="packer_js" src="" type="text/javascript"></script>

6. Create webpack.config.js file with webpack.config.js file data. Update your project entry points with their respective paths. We can give multiple entry points(i.e separate entry point for each app) for the project.  After compressing, separate css, file will be genarated with respective entry point name.


7. Add the following details in settings file about compressing css, js files::

    WEB_PACK_FILES = [
        {'html_file_name': {{ HTML_FILE_RELATIVE_PATH }},
         'webpack_js': {{ WEBPACK_ENTRY_POINT_KEY_NAME }},
        },
        {'html_file_name': {{ HTML_FILE_RELATIVE_PATH }},
         'webpack_js': {{ WEBPACK_ENTRY_POINT_KEY_NAME }},
         },
        {'html_file_name': {{ HTML_FILE_RELATIVE_PATH }}',
         'webpack_js': {{ WEBPACK_ENTRY_POINT_KEY_NAME }},
         },
    ]

8. Run python manage.py compress_css_js_files to generate compressed css, js file. It will updates html file with respective compressed css, js files. Link, script tags will be loaded with compressed css, js files.


9. If you use django storages, then add the following variable to settings file to load compressed css, js files from s3.


    # AWS details

    AWS_ACCESS_KEY_ID = "Your AWS Access Key"

    AWS_SECRET_ACCESS_KEY = "Your AWS Secret Key"

    AWS_BUCKET_NAME = "Your AWS Bucket Name"

    ENABLE_DJANGO_WEBPACK_AWS = True

Modules used:
-------------

    * Django  = 1.9.6


We are always looking to help you customize the whole or part of the code as you like.


Visit our Django Development page `Here`_


We welcome your feedback and support, raise `github ticket`_ if you want to report a bug. Need new features? `Contact us here`_

.. _contact us here: https://micropyramid.com/contact-us/
.. _github ticket: https://github.com/MicroPyramid/django-webpacker/issues
.. _Here: https://micropyramid.com/django-development-services/

    or

mailto:: "hello@micropyramid.com"

