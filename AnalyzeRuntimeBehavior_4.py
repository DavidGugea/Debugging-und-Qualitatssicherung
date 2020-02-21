import pprint
import timeit


def add(range_):
    x = (i for i in range(range_)) 
    a = 0
    for i in x:
        a += i
    return a

timer = timeit.Timer(
    stmt = "add(50)", 
    setup = "from __main__ import add" 
)

n = timer.repeat(100, 10000)

pprint.pprint(n, indent = 60)

for i in range(10):
    print()
    
print("MIN > {0}".format(min(n)))