#!/usr/bin/python
#wrap data in order to fit in pylearn2 yaml
#refer from https://github.com/yyaodong/Pylearn2/blob/master/pylearn2-classification/dataset_wrapper.py
import numpy as np
from pylearn2.datasets.dense_design_matrix import DenseDesignMatrix

def load_data(features, labels, start = 0, stop = None):
    X = np.load(features)
    y = np.load(labels)
    X = X[start:stop, :]
    y = y[start:stop, :]
    return DenseDesignMatrix(X = X, y = y)
