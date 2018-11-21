from arg_retval_counter import ArgReturnCounter
from verb_picker import VerbPicker
from info import Info
import itertools

BIGRAM = 2
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

class WriteInfo:
    __arg_retval_counter = ArgReturnCounter()
    __is_target = bool()
    __info = Info()
    __bigram_opcodes = map(lambda x: "".join(x), list(itertools.product(opcodes, opcodes)))
    __arg_info = [STRING, INT, OBJECT, WRITER, BOOLEAN, LIST, CLASS, ARRAIED_BYTE, LONG, MAP, ARRAIED_STRING, FILE, ARRAIED_OBJECT, ARRAID_CHAR, STRING_BUFFER, COLLECTION, ARRAIED_INT, INPUT_STREAM, DOUBLE, CHAR]
    __return_info = [VOID, BOOLEAN, STRING, INT, OBJECT, LIST]

    def __put_name(self,  name):
        verb_picker = VerbPicker()
        self.__info.set_verb(verb_picker.pick(name))
        if self.__info.verb():
            self.__is_target = True

    def __put_arg(self, args):
        self.__info.set_args_len(len(args))
        vector_args = [0 for _ in xrange(len(self.__arg_info))]
        for arg in args:
            if not arg in self.__arg_info:
                continue
            vector_args[self.__to_index_args(arg)] += 1
        self.__info.set_args(vector_args)

    def __put_return(self, retval):
        vector_return = [0 for _ in xrange(len(self.__return_info))]
        if retval.endswith(";"):
            retval = retval[:-1]
        if retval in self.__return_info:
            vector_return[self.__to_index_return(retval)] += 1
        self.__info.set_retval(vector_return)

    def __put_opcode(self, opcodes):
        vector_opcode = [0 for _ in xrange(len(self.__bigram_opcodes))]
        for i in xrange(0, len(opcodes)-4, BIGRAM):
            vector_opcode[self.__to_index_opcode(opcodes[i:i+4])] += 1
        self.__info.set_opcodes(vector_opcode)

    def __make_info(self, name, args, retval, opcodes):
        self.__put_name(name)
        self.__put_arg(args)
        self.__put_return(retval)
        self.__put_opcode(opcodes)

    def __to_index_args(self, arg):
        return self.__arg_info.index(arg)

    def __to_index_return(self, retval):
        return self.__return_info.index(retval)

    def __to_index_opcode(self, opcode):
        return self.__bigram_opcodes.index(opcode)

    def add(self, name, arg_retval, opcodes):
        args, retval = self.__arg_retval_counter.count(arg_retval)
        self.__make_info(name, args, retval, opcodes)

    def is_target(self):
        return self.__is_target

    def info(self):
        return self.__info

