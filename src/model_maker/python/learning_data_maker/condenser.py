chars = [str(i) for i in xrange(10)] + [chr(i) for i in xrange(97, 97+26)] + [chr(i) for i in xrange(65, 65+26)]

class Condenser:
    def __to_62(self, num):
        if num >= 62:
            return self.__to_62(num/62)+chars[num%62]
        else:
            return chars[num]

    def condense(self, data):
        condensed_data = str()
        for i, v in enumerate(data):
            v = self.__to_62(v)
            if v == "0":
                continue
            if len(v) > 1:
                v = '"%s"' % v
            index = self.__to_62(i)
            if len(index) == 1:
                index = "0" + index
            condensed_data += "%s%s" % (v, index)
        return condensed_data
