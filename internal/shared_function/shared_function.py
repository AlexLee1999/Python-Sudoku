import internal.time.count_time as time


def time_to_int(t):
    mi = t.hour * 60 + t.mi
    seconds = mi * 60 + t.second
    return seconds


def int_to_time(t):
    second = t % 60
    mi = (t % 3600) // 60
    hour = t // 3600
    return time.Time(hour, mi, second)
