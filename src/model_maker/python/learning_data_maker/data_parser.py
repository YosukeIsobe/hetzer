from write_info import WriteInfo


class DataParser:
    def parse_data(self, data):
        name = data[4]
        arg_retval = data[5]
        opcodes = data[8]
        write_info = WriteInfo()
        write_info.add(name, arg_retval, opcodes)
        return write_info

