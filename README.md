# uCode-March-2017 [![Build Status](https://travis-ci.org/TheGreatGatsvim/uCode-March-2017.svg?branch=master)](https://travis-ci.org/TheGreatGatsvim/uCode-March-2017)
## Prerequisites
1. ruby 2.4
..* compass
2. Python 3
..* pip
..* virtualenvwrapper
3. Redis
4. git
## Install
I hardly recommend to install [virtualenvwrapper](http://virtualenvwrapper.readthedocs.io/en/latest/command_ref.html)
```bash
$ mkvirtualenv -p python3 ucode
$ pip install -r requirements.txt
```
## Run
```bash
$ python manage.py celery -A uCode worker -l debug -B
$ python manage.py runserver 0.0.0.0:8000
```
