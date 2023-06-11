import time

time.time()
time.time() // 31556926

import datetime


current = datetime.datetime.now()
print(current)
next_ = current + datetime.timedelta(days=3)
print(next_)
print(type(next_))
print(type(str(current)))
print(str(current))
print(datetime.datetime.utcnow())