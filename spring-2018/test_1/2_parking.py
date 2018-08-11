from random import randint
from math import ceil

####################################

NUM_CASES = 20

TEST_CASE_FORMAT = """
case = Test %d
input = %s
output = /.*%s.*/
"""

####################################


def long_term(weeks, days, hours):
    weeks = ceil(weeks)
    days = ceil(days)
    hours = ceil(hours)

    hour_cost = 2 + (hours - 1) * 1

    if hour_cost > 9:
        hour_cost = 9

    day_cost = days * 9

    if day_cost > 60:
        day_cost = 60

    total = weeks * 60 + day_cost + hour_cost

    return total


def short_term(days, hours, minutes):
    days = ceil(days)
    hours = ceil(hours)
    minutes = ceil(minutes)

    day_cost = days * 32
    minutes = hours * 60 + minutes

    minute_cost = 2 + (ceil((minutes - 30) / 20) * 1)

    if minute_cost < 2:
        minute_cost = 2
    elif minute_cost > 32:
        minute_cost = 32

    total = day_cost + minute_cost

    return total

####################################


for i in range(1, 1 + NUM_CASES):
    lot = randint(0, 1)
    a, b, c = randint(1, 10), randint(1, 10), randint(1, 10)

    if lot == 1:
        cost = long_term(a, b, c)
    else:
        cost = short_term(a, b, c)

    inp = "%d\n%d\n%d\n%d" % (lot, a, b, c)
    out = str(int(cost))

    print(TEST_CASE_FORMAT % (i, inp, out))
