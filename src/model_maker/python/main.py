# coding: utf-8

from argparse import ArgumentParser
from learning_data_maker.learning_data_maker import DateMaker
from model_maker.model_maker import ModelMaker

def parser():
    argparser = ArgumentParser()
    argparser.add_argument('FILE', type=str, help='source data (.csv)')
    argparser.add_argument('-v', '--verb', type=int, metavar='N', help='number of verbs in making model (default: 100)', default=100)
    argparser.add_argument('-t', '--tree', type=int, metavar='N', help='number of trees in the forest (default: 10)', default=10)
    argparser.add_argument('--add', type=str, metavar='V', nargs='*', help='additional verbs (stronger than --remove)', default=list())
    argparser.add_argument('--remove', type=str, metavar='V', nargs='*', help='exclusion verbs', default=list())
    return argparser.parse_args()

def run():
    arguments = parser()
    source_file = arguments.FILE
    additional_verbs = arguments.add
    exclusion_verbs = arguments.remove
    num_of_verbs = arguments.verb
    num_of_trees = arguments.tree
    if len(additional_verbs) > num_of_verbs:
        print "Error: too many additonal verbs."
        return
    data_maker = DateMaker()
    learning_data = data_maker.make(source_file)
    model_maker = ModelMaker(num_of_verbs, additional_verbs, exclusion_verbs, num_of_trees)
    model_maker.make(source_file.split("/")[-1], learning_data)

if __name__ == "__main__":
    run()

