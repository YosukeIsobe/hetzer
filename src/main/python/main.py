import sys
import os
import subprocess
from argparse import ArgumentParser, ArgumentDefaultsHelpFormatter

import method_recommend.recommender as mr
from data.data_parser import Parser

def parser():
    argparser = ArgumentParser()
    argparser.add_argument('MODEL', type=str, help='de-obfuscation model')
    argparser.add_argument('FILE', type=str, help='target data')
    argparser.add_argument('-l', '--lower', metavar='N', type=int, help='lower of birthmark length (default: None)', default=None)
    argparser.add_argument('-u', '--upper', metavar='N', type=int, help='upper of birthmark length (default: None)', default=None)
    return argparser.parse_args()

def get_lines(cmd):
    proc = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    while True:
        line = proc.stdout.readline()
        if line:
            yield line
        if not line and proc.poll() is not None:
            break

def write_results(recommender, jar, lower, upper):
    recommender = mr.recommender(recommender, lower, upper)
    parser = Parser()
    for line in get_lines(cmd="java -jar build/libs/hetzer.jar %s" % jar):
        target, predictor_variable = parser.parse(*line.split(","))
        method = recommender.recomend(predictor_variable)
        sys.stdout.write("%s," % target)
        sys.stdout.write("%s\n" % method)

if __name__ == '__main__':
    arguments = parser()
    jar = arguments.FILE
    recommender = arguments.MODEL
    lower = arguments.lower
    upper = arguments.upper
    write_results(recommender, jar, lower, upper)

