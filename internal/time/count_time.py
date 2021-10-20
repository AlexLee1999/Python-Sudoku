import internal.shared_function.shared_function as shared


class Time(object):
    def __init__(self, hour, mi, second):
        self.second = second
        self.mi = mi
        self.hour = hour

    def __str__(self):
        return ('Time %.2d:%.2d:%.2d' % (self.hour, self.mi, self.second))

    def __add__(self, other):
        t = self.second + self.mi * 60 + self.hour * 3600
        q = t + other
        return shared.int_to_time(q)
