class LoggableList(list, Loggable):
    def append(self, p_object):
        self.log(p_object)
        super().append(p_object)
