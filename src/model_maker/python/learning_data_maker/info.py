class Info:
    __verb = str()
    __args_len = int()
    __args = list()
    __retval = list()
    __opcodes = list()

    def set_verb(self, verb):
        self.__verb = verb

    def verb(self):
        return self.__verb

    def set_args_len(self, args_len):
        self.__args_len = args_len

    def args_len(self):
        return self.__args_len

    def set_args(self, args):
        self.__args = args

    def args(self):
        return self.__args

    def set_retval(self, retval):
        self.__retval = retval

    def retval(self):
        return self.__retval

    def set_opcodes(self, opcodes):
        self.__opcodes = opcodes

    def opcodes(self):
        return self.__opcodes

    def __make_info(self):
        normalized_info = list()
        normalized_info.append(self.args_len())
        normalized_info += self.args()
        normalized_info += self.retval()
        normalized_info += self.opcodes()
        return normalized_info

    def normalize(self):
        return self.__make_info()
