#!/usr/bin/env python
# -*- coding: utf-8 -*-
import numpy as np
from sklearn.ensemble import RandomForestClassifier


# learninig data
data_training = np.loadtxt('data/train-images.txt', delimiter=' ')
label_training = np.loadtxt('data/train-labels.txt')

# test data
data_test = np.loadtxt('data/test-images.txt', delimiter=' ')

# learn
#estimator = LinearSVC(C=1.0)
estimator = RandomForestClassifier()
estimator.fit(data_training, label_training)

# test
label_prediction = estimator.predict(data_test)



[ print(i) for i in label_prediction ]


