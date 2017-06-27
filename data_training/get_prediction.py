# Referring 
# https://github.com/yyaodong/Pylearn2/blob/master/
# pylearn2-classification/predict_csv.py
import sys
import os
import argparse
import numpy as np

from pylearn2.utils import serial
from theano import tensor as T
from theano import function

def make_parser():
    '''
    Parses the parameters from sys.argv of this script
    '''
    parser = argparse.ArgumentParser(
        description = "Prediction from a pkl file, default:\n" +\
        "python get_prediction.py framework_best.pkl test_feautures.npy output.txt\n" +\
        "or\n" +\
        "python get_prediction.py\n" +\
        "for default configuration..."
        )
    parser.add_argument('model_filename', 
        help = 'Specifies the pkl model file',
        nargs = '?',
        const = 1,
        default = "framework_best.pkl")
    parser.add_argument('test_filename', 
        help = 'Specifies the npy input file',
        nargs = '?',
        const = 1,
        default = "test_features.npy")
    parser.add_argument('output_filename',
        help = 'Specifies the prediction output file',
        nargs = '?',
        const = 1,
        default = "output.txt")
    return parser

def predict(model_filename, test_filename, output_filename):
    print("Loading model...")
    try:
        model = serial.load(model_filename)
    except Exception as e:
        print("Error on loading {}:".format(model_filename))
        print(e)
        return False

    print("Setting up symbolic expressions...")

    X = model.get_input_space().make_theano_batch()
    # getting label
    Y = model.fprop(X)
    # getting Prob
    M = model.fprop(X)
    
    # getting the maximum number for each line
    Y = T.argmax(Y, axis = 1)

    f = function([X], Y, allow_input_downcast = True)

    f_prob = function([X], M, allow_input_downcast = True)

    print("Loading data and predicting...")

    # load test data in numpy format
    x = np.load(open(test_filename, 'rb'))
    
    y = f(x)

    m = f_prob(x)

    print("Writing predictions...")

    np.savetxt(output_filename, y, fmt = "%d")
    np.savetxt("".join(["Prob_", output_filename]), m, fmt = "%f")
    return True

if __name__ == "__main__":
    parser = make_parser()
    args = parser.parse_args()
    ret = predict(args.model_filename, args.test_filename, args.output_filename)
    if not ret:
        sys.exit(-1)