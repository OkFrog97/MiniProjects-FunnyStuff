import time


class Loggable:
    def log(self, msg):
        print(str(time.ctime()) + ": " + str(msg))
        

class LoggableList(list, Loggable):
    def append(self, p_object):
        self.log(p_object)
        super().append(p_object)


def test():
    t = LoggableList()
    t.append(1)
    t.append('str')
    assert len(t) == 2


if __name__ == "__main__":
    test()