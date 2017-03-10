# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
# import pandas as pd
# import numpy as np
from sklearn import datasets, tree
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from celery.signals import celeryd_after_setup
from uCode.celery import app

import pydotplus


def print_pdf(self, filename="decisionTree.pdf"):
    dot_data = tree.export_graphviz(self.classifier,
                                    out_file=None,
                                    feature_names=self.data.feature_names,
                                    class_names=self.data.target_names,
                                    filled=True,
                                    rounded=True,
                                    special_characters=True)
    graph = pydotplus.graph_from_dot_data(dot_data)
    graph.write_pdf(filename)


@app.task(trail=True)
@celeryd_after_setup.connect
def train(**kwargs):
    # TODO: download and parse dataset
    data = datasets.load_iris()
    X = data.data
    y = data.target
    # TODO: store data in db

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=.5)
    # TODO: store X_train, X_test, y_train, y_test in db
    print("-"*9)
    print(X_train, X_test, y_train, y_test)
    print("-"*9)


@app.task(trail=True)
def predict(X_train, X_test, y_train, y_test):
    classifier = tree.DecisionTreeClassifier()
    classifier.fit(X_train, y_train)

    predictions = classifier.predict(X_test)
    accuracy = accuracy_score(y_test, predictions)
    # TODO: store predictions and accuracy in db
    print(predictions, accuracy)


@app.task(trail=True)
def dummy_plus(a, b):
    return a + b
