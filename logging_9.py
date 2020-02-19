import logging
import sys

handler = logging.StreamHandler(stream = sys.stdout)

formatter = logging.Formatter(
    fmt = "{asctime} [Level name : {levelname} // Line number : {lineno}] ===== > {message}",
    datefmt = "%d.%m.%Y : %H:%M:%S",
    style="{"
)
handler.setFormatter(formatter)

logger = logging.getLogger()
logger.addHandler(handler)
logger.setLevel(logging.DEBUG)

def quickSort(arr, low, high):
    if low < high:
        partitionSplitIndex = partition(arr, low, high)

        quickSort(arr, low, partitionSplitIndex-1)
        quickSort(arr, partitionSplitIndex+1, high)
def partition(arr, low, high):
    i = low
    pivot = arr[high]

    logger.info("i : {0} // pivot : {1}".format(i, pivot    ))
    for j in range(low, high, 1):
        if arr[j] < pivot:
            # Reverse values
            arr[i], arr[j] = arr[j], arr[i]
            # Increment *| i |* index value
            i += 1

    # Reverse the pivot value with the *| i |* index value
    arr[i], arr[high] = arr[high], arr[i]

    # Return the partition split index
    return i

RANGE_STOP = eval(input("RANGE STOP > "))
n = list(range(1, RANGE_STOP+1, 1))[::-1]
print("Array before quick sort : {0}".format(n))
quickSort(n, 0, len(n)-1)
print("Array after quick sort : {0}".format(n))