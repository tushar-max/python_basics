import time

# print(time.time())

# how long a piece of code takes to run

def calcProd():
    # Calculate the product of the first 100,000 numbers
    product = 1
    for i in range(1,1000):
        product *= i
    return product

startTime = time.time()
prod = calcProd()
endTime = time.time()

print('The result is %s digits long.' % (len(str(prod))))
# Calculate the time to run the program:
print('Took %s seconds to calculate.' % (endTime - startTime))

print(time.ctime())

# Pause a Program
"""
for i in range(3):
    print("tick")
    time.sleep(1)
    print("tock")
    time.sleep(1)
"""

import datetime

dt = datetime.datetime.now()

print(dt)
print(dt.year, dt.month, dt.day,sep="/")

# A Unix epoch timestamp can be converted to a datetime object with the datetime.datetime.fromtimestamp() function

print(datetime.datetime.fromtimestamp(time.time()))

# You can compare datetime objects with each other using comparison operators to find out which one precedes the other.

halloween2019 = datetime.datetime(2019,10,31)
newYear2020 = datetime.datetime(2020,1,1)

print(halloween2019 < newYear2020)

