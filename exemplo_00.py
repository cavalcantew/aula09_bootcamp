from log import log_decorator
from timer import time_measure_decorator
import time

@time_measure_decorator
def soma(x, y):
    time.sleep(5)
    return x + y

soma(2,5)
soma(5,12)