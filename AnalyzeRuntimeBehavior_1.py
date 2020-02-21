import gc
import pprint
import timeit

gc.enable()

def fak1(n):
    res = 1 
    for i in range(2, n+1):
        res *= i 
    return res
def fak2(n):
    if n > 0:
        return fak2(n-1)*n
    else:
        return 1
    
t1 = timeit.Timer("fak1(50)", "from __main__ import fak1")
t2 = timeit.Timer("fak2(50)", "from __main__ import fak2")

print("Iterativ : {0}".format(t1.timeit(10000)))
print("Rekursiv : {0}".format(t2.timeit(10000)))

for i in range(10):
    print() 
    
print("Iterativ :")
pprint.pprint(t1.repeat(100, 10000), indent=100)
print(len(t1.repeat(100, 10000)))

for i in range(10):
    print()
    
print("Recursive :")
pprint.pprint(t2.repeat(100, 10000), indent=100)
print(len(t2.repeat(100, 10000)))
