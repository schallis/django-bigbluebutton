====================
django-bigbluebutton
====================
:Info: A Django project for interacting with BigBlueButton
:Author: Steve Challis (http://schallis.com)
:Requires: BigBlueButton >= 0.71, Django >= 1.0

This is a simple Django project and application that interacts with the
`BigBlueButton <http://bigbluebutton.org>`_ API to allow you to create and
interact with web conference meetings  It currently supports:

* Password protected administration
* Meeting creation/ending
* Meeting joining
* List all currently running meetings


Setup
=====
You'll first need to edit settings.py in the bbb_django project or your own
project. The following custom variables must be added/set:

* SALT = "[your_salt]"
* BBB_API_URL = "http://yourdomain.com/bigbluebutton/api/"

The `bbb` application is where all the controllers and views are contained so
you should be able to drop this into any Django project.

You can quickly test the project with the Django default webserver but you'll
probably want to have it running permenantly. `Gunicorn
<http://http://gunicorn.org/>`_ has already been added in as a dependancy so
you should be able to use `gunicorn_django` once gunicorn is installed.

It is assumed you are using FreeSWITCH for the voice calling but it is easy
enough to change the extension to that required by Asterisk.

Screenshots
===========
.. image:: https://github.com/schallis/django-bigbluebutton/raw/master/screenshots/screenshot-create.png

.. image:: https://github.com/schallis/django-bigbluebutton/raw/master/screenshots/screenshot-meetings.png
