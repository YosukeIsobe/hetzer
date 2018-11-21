import sys
import os
sys.path.append(os.path.abspath(".")+"/libs/python/2.7/site-packages")
import numpy as np
from data_maker import Maker
from arg_retval_counter import Counter

class Parser:
    def parse(self, method_name, arg_retval, opcodes):
        maker = Maker()
        counter = Counter()
        args, retval = counter.count(arg_retval)
        data = maker.make(method_name, args, retval, opcodes)
        target = data[0]
        predictor_variable = np.array(data[1:])
        return target, predictor_variable
