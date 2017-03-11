# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from celery.signals import celeryd_after_setup
from uCode.celery import app
from sneakers.models import Sneaker
from django.core import files
import requests
import tempfile


@app.task(trail=True)
def save_sneaker(label, url):
    request = requests.get(url, stream=True)
    file_name = url.split('/')[-1]
    lf = tempfile.NamedTemporaryFile()
    for block in request.iter_content(1024 * 8):
        if not block:
            break
        lf.write(block)

    sneaker = Sneaker()
    sneaker.label = label
    sneaker.feature.save(file_name, files.File(lf))
    sneaker.save()


@app.task(trail=True)
@celeryd_after_setup.connect
def train(**kwargs):
    print("train")


@app.task(trail=True)
def predict(X_train, X_test, y_train, y_test):
    print("predict")


@app.task(trail=True)
def dummy_plus(a, b):
    return a + b
