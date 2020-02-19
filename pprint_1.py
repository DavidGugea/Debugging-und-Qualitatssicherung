import pprint
import sys

print("Pprint :")
pprint.pprint(sys.path)

for i in range(3):
    print()

print("Print :")
print(sys.path)

for i in range(10):
    print()

#pprint.pprint(sys.path, stream=sys.stdout, indent=5, width=5, depth=100, compact=2)
pprint.pprint(sys.path, indent=15)