Installation
=============

Note
----

1. Create a python virtual environment (so the deps don't get installed into your system python directory)

	`$ curl -O https://raw.github.com/pypa/virtualenv/master/virtualenv.py`

	`$ python virtualenv.py my_new_env`
	`$ . my_new_env/bin/activate`


1. Download & install distribute

	`$ curl http://python-distribute.org/distribute_setup.py | python`

2. Download & install pip

	`$ curl https://raw.github.com/pypa/pip/master/contrib/get-pip.py | python`

3. Install the dependencies:

	`$ pip install -r requirements.txt`

Usage
---

This demo uses [Fabric][1] as an execution tool - you'll get the idea when you look at fabfile.py.

It uses the [nosetests][2] library as an test discovery and execution thing.

It looks at the app.core.config.xml library in the application-core directory and runs two very simple structural tests on them.


[1]:http://docs.fabfile.org/en/latest/index.html
[2]:http://nose.readthedocs.org/en/latest/

