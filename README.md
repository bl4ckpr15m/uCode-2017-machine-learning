# uCode-March-2017 [![Build Status](https://travis-ci.org/TheGreatGatsvim/uCode-March-2017.svg?branch=master)](https://travis-ci.org/TheGreatGatsvim/uCode-March-2017)
## Prerequisites
1. ruby 2.4
  * compass
  
2. Python 3
  * pip
  * virtualenvwrapper
  
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
## Local settings
Change the xxx credentials with your own ones. Store it in uCode/local_settings.py
```python
from pytumblr import TumblrRestClient
from twitter import Api


# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'xxx'

twitter_api = Api(consumer_key='xxx',
        consumer_secret='xxx',
        access_token_key='xxx-xxx',
        access_token_secret='xxx',
        tweet_mode='extended')


consumer_key = "xxx"
consumer_secret = "xxx"
token = "xxx"
token_secret = "xxx"
api_key = "xxx"

tumblr_api = TumblrRestClient(consumer_key,
        consumer_secret,
        token,
        token_secret)

telegram_token="xxx:xxx"

BROKER_URL = 'redis://localhost:6379'
CELERY_RESULT_BACKEND = 'redis://localhost:6379'
CELERY_ACCEPT_CONTENT = ['application/json']
CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'
CELERY_TIMEZONE = 'Europe/Madrid'
CELERY_RESULT_BACKEND = 'djcelery.backends.database:DatabaseBackend'
CELERYBEAT_SCHEDULER = 'djcelery.schedulers.DatabaseScheduler'

```
