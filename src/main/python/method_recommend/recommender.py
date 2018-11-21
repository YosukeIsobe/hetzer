import sys
import os
sys.path.append(os.path.abspath(".")+"/libs/python/2.7/site-packages")
import numpy as np
from sklearn.externals import joblib


class recommender:
    __model = None
    __upper_length = int()
    __lower_length = int()


    def __init__(self, source, lower, upper):
        self.__model = joblib.load(source)
        self.__lower_length = lower
        self.__upper_length = upper

    def recomend(self, predictor_variable):
        length = sum(predictor_variable[-(36**2):])
        if not self.__check_lower(length) or not self.__check_upper(length):
            return "birthmark out of bounds"
        return self.__model.predict(np.array([predictor_variable]))[0]

    def __check_lower(self, length):
        if type(self.__lower_length) == int:
            return length >= self.__lower_length
        return True
    def __check_upper(self, length):
        if type(self.__upper_length) == int:
            return length <= self.__upper_length
        return True
