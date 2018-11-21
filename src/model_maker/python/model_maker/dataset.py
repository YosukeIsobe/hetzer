import csv
from collections import defaultdict
from tqdm import tqdm

from thawer import Thawer

TARGET = 0

class Dataset:
    __additional_verbs = list()
    __exclusion_verbs = list()

    def __init__(self, additional_verbs, exclusion_verbs):
        self.__additional_verbs = additional_verbs
        self.__exclusion_verbs = exclusion_verbs

    def __filter_verb(self, learning_data, num_of_verbs):
        freq = defaultdict(int)
        verbs = list()
        total = 0
        with open(learning_data, "r") as reader:
            for line in reader:
                verbs.append(line.split(",")[0])
                total += 1
        for verb in verbs:
            freq[verb] += 1
        target_verb = self.__additional_verbs
        for verb, freq in sorted(freq.items(), key=lambda x:x[1], reverse=True):
            if len(target_verb) == num_of_verbs:
                break
            if verb in self.__exclusion_verbs:
                continue
            if not verb in target_verb:
                target_verb.append(verb)
        return target_verb, total

    def __read_data(self, learning_data, target_verb, total):
        print "Reading learning data at %s" % learning_data
        bar = tqdm(total=total)
        with open(learning_data, "r") as reader:
            count = 0
            del_count = 0
            target = list()
            values = list()
            row = list()
            col = list()
            thawer = Thawer()
            for i, line in enumerate(reader):
                bar.update(1)
                verb, v, n = thawer.thaw(line)
                if not verb in target_verb:
                    continue
                for i in xrange(len(v)):
                    values.append(int(v[i]))
                    row.append(count)
                    col.append(n[i])
                target.append(verb)
                count += 1
        return target, values, row, col

    def read(self, learning_data, num_of_verbs):
        target_verb, total = self.__filter_verb(learning_data, num_of_verbs)
        target, values, row, col = self.__read_data(learning_data, target_verb, total)
        retval = {
            "target": target,
            "values": values,
            "row": row,
            "col": col
        }
        return retval
