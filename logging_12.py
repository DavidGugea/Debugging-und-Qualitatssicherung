import logging
import pprint
import sys

stream = logging.StreamHandler(stream=sys.stdout)

formatter = logging.Formatter(
    fmt = "{asctime} [ Levelname : {levelname} || Line number : {lineno} ] == > {message}",
    datefmt = "%d.%m.%Y < - > %H:%M:%S",
    style = "{"
)
stream.setFormatter(formatter)

logger = logging.getLogger()
logger.addHandler(stream)
logger.setLevel(logging.DEBUG)

def partition(arr, low, high):
    i = low
    pivot = arr[high] 
    
    for j in range(low, high):
        if arr[j] < pivot:
            # Swap i and j and increment i
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
    
    # Swap the pivot with the | i | index value
    arr[i], arr[high] = arr[high], arr[i]
    
    # Return the i =~ partition index splitter
    return i
    
def quickSort(arr, low, high):
    if low < high:
        partitionIndexSplitter = partition(arr, low, high)
        
        logger.info("arr : {0} // partitionIndexSplitter : {1} // low : {2} // high : {3}".format(
            arr,
            partitionIndexSplitter,
            low,
            high
        ))
        
        quickSort(arr, partitionIndexSplitter+1, high)
        quickSort(arr, low, partitionIndexSplitter-1)
    else:
        logger.critical("low < high || low ( {0} ) < high ( {1} )".format(
            low,
            high
        ))


while True:
    try:
        RANGE_STOP = eval(input("RANGE STOP > "))
         
        if RANGE_STOP <= 0:
            raise Exception
        else:
            break
    except Exception as __error__:
        logger.fatal("RANGE_STOP < 0 or not a number")
    
logger.info("RANGE_STOP : {0}".format(RANGE_STOP))
n = list(range(1, RANGE_STOP+1, 1))[::-1]
pprint.pprint(n, indent=10)
quickSort(n, 0, len(n)-1)

for i in range(5):
    print()

print("n after quick sort :")
pprint.pprint(n, indent=10)