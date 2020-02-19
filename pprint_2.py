import pprint
import sys

s = pprint.pformat(sys.path)

print(s)

for i in range(3):
    print() 

print(type(s))