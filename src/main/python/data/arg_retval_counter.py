import csv
import sys
from collections import defaultdict

class Counter:
    def __is_java_std(self, arg):
        return arg.startswith("Ljava")
    def __is_java_lui(self, arg):
        return arg.startswith("Ljava/io") or arg.startswith("Ljava/util") or arg.startswith("Ljava/lang")
    def __is_object(self, arg):
        return arg[0] == "L"
    def __is_list(self, arg):
        return arg[0] == "["
    def __parse_args(self, args):
        if not args:
            return list()
        i = 0
        list_count = 0
        li = list()
        args_length = len(args)
        while args_length > i:
            if self.__is_list(args):
                list_count += 1
                args = args[1:]
                i += 1
                continue
            if self.__is_object(args):
                if not self.__is_java_lui(args):
                    return li
                li.append("".join(["[" for _ in xrange(list_count)])+args)
                return li
            li.append("".join(["[" for _ in xrange(list_count)])+args[0])
            args = args[1:]
            i += 1
            list_count = 0
        return li

    def count(self, arg_retval):
        arg, retval = arg_retval.split(")")
        arg = arg[1:]
        if ";" in arg:
            args = arg.split(";")[:-1]
        else:
            args = [arg]
        return [arg for group in args for arg in self.__parse_args(group)], retval
