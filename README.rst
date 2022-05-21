=====
 gp2
=====

*Another experiment in defying the Second Law of Thermodynamics.*


Background
==========

This project is an attempt to migrate `my personal site <https://guillaumepaumier.com>`__ from WordPress to a static site using `Nikola <https://getnikola.com>`__.


Install and build
=================

See also the `Getting started <https://getnikola.com/getting-started.html>`_ page in the documentation for Nikola.

Install system packages:

::

    # zypper in libjpeg8-devel libxml2-devel libxslt-devel python3-dbm

Install Python packages:

::

    # pip install --upgrade virtualenv

Set up the virtualenv:

::

    $ virtualenv nikola
    $ cd nikola
    $ source bin/activate

Install Nikola and extras:

::

    $ pip install --upgrade pip setuptools wheel
    $ pip install --upgrade "Nikola[extras]"

Clone the site's repository:

::

    $ git clone git@github.com:gpaumier/gp2.git

Once in the site's directory: Install Nikola plugins as needed:

::

    $ nikola plugin -i sphinx_roles



Build the site :

::

    $ nikola build

and launch the built-in webserver:

::

    $ nikola serve

Or launch in watcher+server mode:

::

    $ nikola auto


Developing the theme
====================

I'm currently using `Brunch <http://brunch.io/>`__ to compile JavaScript and CSS assets. This is only needed to modify the site's JS and CSS; when writing and publishing a new post or page, the theme doesn't change so the previous section is enough.

Install Brunch globally:

::

    # npm install -g brunch


From the site's directory, install the theme's dependencies:

::

    $ npm install -D

Launch Brunch in watcher mode:

::

    $ brunch watch

Or build assets with a one-off command:

::

    $ brunch build

Bits (JS and CSS) compiled by Brunch will be picked up by brunch and compiled, then Nikola will update its build folder, if it's simultaneously running in ``auto`` mode; otherwise, ``build`` manually.

Maintenance stuff:

::

      $ npm outdated

Building for deployment
=======================

* `Install Docker <https://en.opensuse.org/Docker>`__

* Set up the `local build container <https://github.com/netlify/build-image#available-images>`__
