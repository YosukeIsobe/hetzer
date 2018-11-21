import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.externals import joblib
import scipy

from dataset import Dataset

class ModelMaker:
    __num_of_verbs = int()
    __additional_verbs = list()
    __exclusion_verbs = list()
    __num_of_trees = int()

    def __init__(self, num_of_verbs, additional_verbs, exclusion_verbs, num_of_trees):
        self.__num_of_verbs = num_of_verbs
        self.__additional_verbs = additional_verbs
        self.__exclusion_verbs = exclusion_verbs
        self.__num_of_trees = num_of_trees

    def make(self, source_file, learning_data):
        dataset = Dataset(self.__additional_verbs, self.__exclusion_verbs)
        data = dataset.read(learning_data, self.__num_of_verbs)

        y = np.array(data["target"])
        values = np.array(data["values"])
        row = np.array(data["row"])
        col = np.array(data["col"])
        x = scipy.sparse.coo_matrix((values, (row, col)), shape=(len(y), 1323))
        model = RandomForestClassifier(n_estimators=self.__num_of_trees)
        print "Making model..."
        model.fit(x.tocsr(), y)
        joblib.dump(model, "src/main/resources/%s.pkl" % source_file, compress=True)
