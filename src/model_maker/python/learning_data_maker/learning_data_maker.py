import sys
import os
sys.path.append(os.path.abspath(".")+"/libs/python/2.7/site-packages")
import csv
from data_parser import DataParser
from tqdm import tqdm

from condenser import Condenser

class DateMaker:
    def __make_learning_data(self, source_file, writer):
        total = 0
        with open(source_file, "r") as f:
            for _ in f:
                total += 1
        print "Making learning data"
        bar = tqdm(total=total)
        with open(source_file, "r") as reader:
            parser = DataParser()
            condenser = Condenser()
            for line in csv.reader(reader):
                bar.update(1)
                write_info = parser.parse_data(line)
                if not write_info.is_target():
                    continue
                verb = write_info.info().verb()
                data = write_info.info().normalize()
                writer.write(('%s,' % verb) + condenser.condense(data) + "\n")

    def make(self, source_file):
        save_data = "./src/model_maker/resources/%s.pika" % source_file.split("/")[-1]
        if os.path.exists(save_data):
            return save_data
        if not os.path.exists("./src/model_maker/resources"):
            os.makedirs("./src/model_maker/resources")
        with open(save_data, "w") as writer:
            self.__make_learning_data(source_file, writer)
        return save_data
