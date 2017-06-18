import sys
import os
sys.path.append(os.path.abspath(".")+"/libs/python/lib/python/site-packages/")
import numpy as np

def parse(data):
    objective_variable = data[0]
    predictor_variable = np.array(list(data[1:]))
    try:
        predictor_variable[-1] = predictor_variable[-1][:-1]
    except:
        return objective_variable[:-1], []
    return objective_variable, predictor_variable
