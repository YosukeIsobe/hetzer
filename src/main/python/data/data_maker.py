# coding: utf-8

import sys
import csv
import itertools

BIGRAM= 2
ARRAY = "["

INT = "I"
DOUBLE = "D"
LONG = "J"
BOOLEAN = "Z"
CHAR = "C"
VOID = "V"
STRING = "Ljava/lang/String"
OBJECT = "Ljava/lang/Object"
CLASS = "Ljava/lang/Class"
WRITER = "Ljava/io/Writer"
LIST = "Ljava/util/List"
MAP = "Ljava/util/Map"
COLLECTION = "Ljava/util/Collection"
STRING_BUFFER = "Ljava/util/StringBuffer"
FILE = "Ljava/io/File"
INPUT_STREAM = "Ljava/io/InputStream"
ARRAIED_BYTE = "[B"
ARRAIED_INT = ARRAY+INT
ARRAIED_STRING = ARRAY+STRING
ARRAIED_OBJECT = ARRAY+OBJECT
ARRAID_CHAR = ARRAY+CHAR


opcodes = ["00", "01", "19", "2e", "36", "4f", "57", "59", "5f", "60", "64", "68", "6c", "70", "74", "78", "7a", "7c", "7e", "80", "82", "87", "94", "a7", "b1", "ab", "b4", "b6", "bb", "bc", "be", "bf", "c0", "c1", "c2", "c4"]
bigram_opcodes = map(lambda x: "".join(x), list(itertools.product(opcodes, opcodes)))

arg_info = [STRING, INT, OBJECT, WRITER, BOOLEAN, LIST, CLASS, ARRAIED_BYTE, LONG, MAP, ARRAIED_STRING, FILE, ARRAIED_OBJECT, ARRAID_CHAR, STRING_BUFFER, COLLECTION, ARRAIED_INT, INPUT_STREAM, DOUBLE, CHAR]

return_info = [VOID, BOOLEAN, STRING, INT, OBJECT, LIST]

class Maker:
    def __to_index_ar(self, arg):
        return 2+arg_info.index(arg)

    def __to_index_re(self, retval):
        return 2+len(arg_info)+return_info.index(retval)

    def __to_index_op(self, opcode):
        return 2+len(arg_info)+len(return_info)+bigram_opcodes.index(opcode)

    def __put_name(self, write, name):
        write[0] = name
        return

    def __put_arg(self, write, args):
        write[1] = len(args)
        for arg in args:
            if not arg in arg_info:
                continue
            write[self.__to_index_ar(arg)] += 1
        return

    def __put_return(self, write, retval):
        if retval.endswith(";"):
            retval = retval[:-1]
        if not retval in return_info:
            return
        write[self.__to_index_re(retval)] += 1
        return

    def __put_opcode(self, write, opcodes):
        for i in xrange(0, len(opcodes)-4, BIGRAM):
            write[self.__to_index_op(opcodes[i:i+4])] += 1
        return

    def make(self, name, args, retval, opcodes):
        write = [0 for i in xrange(28+36**2)]
        self.__put_name(write, name)
        self.__put_arg(write, args)
        self.__put_return(write, retval)
        self.__put_opcode(write, opcodes)
        return write

"""
learning data information

0: method name
1: number of args
2: arg java/lang/String
3: arg int
4: arg java/lang/Object
5: arg java/io/Writer
6: arg boolean
7: arg java/util/List
8: arg java/lang/Class
9: arg arraied byte
10: arg long
11: arg java/util/Map
12: arg arraied java/lang/String
13: arg java/io/File
14: arg arraied java/lang/Object
15: arg arraied char
16: arg java/lang/StringBuffer
17: arg java/util/Collection
18: arg arraied int
19: arg java/io/InputStream
20: arg double
21: arg char
22: return void
23: return boolean
24: return java/lang/String
25: return int
26: return java/lang/Object
27: return java/util/List
28: opcode 0000
29: opcode 0001
=======
28+36^2: opcode c4c4
"""
