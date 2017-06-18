import sys
import os
sys.path.append(os.path.abspath(".")+"/libs/python/lib/python/site-packages/")
import numpy as np
from sklearn.externals import joblib


class recommender:
    __models = []
    __mapping_table = {}

    def __init__(self, mapping_table):
        self.__mapping_table = mapping_table
        for i in xrange(2,11):
            self.__models.append(joblib.load("./src/main/resources/%d00.pkl" % i))

    def recomend(self, predictor_variable):
        length = len(predictor_variable)
        if not self.__check_length(length):
            return "birthmark out of bounds"
        length, model = self.__decide_length(length)
        predictor_variable = self.__fill_deficit(predictor_variable, length)
        return self.__mapping_table[model.predict(np.array([predictor_variable]))[0]]

    def __fill_deficit(self, predictor_variable, length):
        while len(predictor_variable) < length-1:
            predictor_variable = np.append(predictor_variable, [-1])
        return predictor_variable

    def __check_length(self, length):
        if length < 100:
            return False
        if length > 1000:
            return False
        return True

    def __decide_length(self, length):
        hundreds_place = length / 100
        if not hundreds_place == 10:
            hundreds_place += 1
        model = self.__models[hundreds_place-2]
        return hundreds_place*100, model

        #
        # y_train_pred = model.predict(x_train)
        # y_test_pred = model.predict(x_test)

        # correct = []
        # fault = []
        # for test, test_pred in zip(y_test, y_test_pred):
        #     if test != test_pred:
        #         fault.append([0, table[str(test)], table[str(test_pred)]])
        #     else:
        #         correct.append([1, table[str(test)], table[str(test_pred)]])
        # print "fault:"
        # for i in fault:
        #     print i
        # print "correct:"
        # for i in correct:
        #     print i

        # print y_test
        # print y_test_pred
        # fault_freq = defaultdict(int)
        # correct_freq = defaultdict(int)
        # for f in fault:
        #     fault_freq[f[1]] += 1
        # for c in correct:
        #     correct_freq[c[1]] += 1
        # print "fault:"
        # for key, value in reversed(sorted(fault_freq.items(), key=lambda x: x[1])):
        #     print "%s => %d" % (key, value)
        # print
        # print "correct:"
        # for key, value in reversed(sorted(correct_freq.items(), key=lambda x: x[1])):
        #     print "%s => %d" % (key, value)

        # print('MSE train : %.3f, test : %.3f' % (mean_squared_error(y_train, y_train_pred), mean_squared_error(y_test, y_test_pred)) )
        # print('R^2 train : %.3f, test : %.3f' % (r2_score(y_train, y_train_pred), r2_score(y_test, y_test_pred)) )
        # print confusion_matrix(y_test, y_test_pred)

