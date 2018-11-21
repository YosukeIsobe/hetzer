chars = [str(i) for i in xrange(10)] + [chr(i) for i in xrange(97, 97+26)] + [chr(i) for i in xrange(65, 65+26)]

class Thawer:
    def __to_10(self, num):
        if len(num) > 1:
            return self.__to_10(num[:-1])*62+chars.index(num[-1])
        else:
            return chars.index(num)

    def thaw(self, condensed_info):
        verb, condensed_info = condensed_info.split(",")
        values = list()
        n = list()
        quotation_flag = False
        value_flag = True
        index = str()
        for char in condensed_info[:-1]:
            if value_flag:
                if quotation_flag:
                    if char == '"':
                        quotation_flag = False
                        value_flag = False
                        values.append(self.__to_10(value))
                    else:
                        value += char
                elif char == '"':
                    value = str()
                    quotation_flag = True
                else:
                    value_flag = False
                    values.append(self.__to_10(char))
            else:
                index += char
                if len(index) == 2:
                    n.append(self.__to_10(index))
                    index = str()
                    value_flag = True
        return verb, values, n

