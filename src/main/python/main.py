import sys
import os
import subprocess

import method_recommend.recommender as mr
import datas.mapping_table as mt
import datas.data_parser as dp


def get_lines(cmd):
    proc = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    while True:
        line = proc.stdout.readline()
        if line:
            yield line
        if not line and proc.poll() is not None:
            break

if __name__ == '__main__':
    args = sys.argv
    if len(args) < 2:
        sys.exit()
    mapping_table = mt.read()
    recommender = mr.recommender(mapping_table)
    for jar in args[1:]:
        for line in get_lines(cmd="java -jar build/libs/hetzer.jar %s" % jar):
            objective_variable, predictor_variable = dp.parse(line.split(","))
            method = recommender.recomend(predictor_variable)
            # if not "birthmark" in method:
                # if objective_variable.split("#")[-1][0] == method[0]:
                #     sys.stdout.write("%s\t->\t" % objective_variable.split("#")[-1])
                #     sys.stdout.write("%s\n" % method)
            sys.stdout.write("%s," % objective_variable)
            sys.stdout.write("%s\n" % method)

