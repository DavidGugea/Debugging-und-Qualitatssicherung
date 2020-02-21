import gc
import logging
import pprint
import sys
import timeit
from concurrent import futures

gc.enable()

streamHandler = logging.StreamHandler(stream = sys.stdout)
formatter = logging.Formatter(
    fmt = "{asctime} [ Level name : {levelname} || Line number : {lineno} ] == > {message}",
    datefmt = "%d.%m.%Y < - > %H:%M:%S",
    style = "{"
)
streamHandler.setFormatter(formatter)

logger = logging.getLogger()
logger.addHandler(streamHandler)
logger.setLevel(logging.DEBUG)

class bubbleSort(object):
    def __init__(self):
        pass
    def bubbleSort_noThreading(self, range_):
        self.range_ = range_
        self.arr = list(range(1, self.range_+1, 1))[::-1]
        
        for i in range(0, len(self.arr)+1, 1):
            swapped = False
            for j in range(0, len(self.arr)-i-1, 1):
                if self.arr[j] > self.arr[j+1]:
                    # Swap items
                    self.arr[j], self.arr[j+1] = self.arr[j+1], self.arr[j]
                    swapped = True
            
            if not swapped:
                break
            else:
                continue
        
        return self.arr
    def bubbleSort_withThreading(self, range_):
        self.range_ = range_
        self.arr = list(range(1, self.range_+1, 1))[::-1]
        
        self.threadExecutor = futures.ThreadPoolExecutor(max_workers = len(self.arr)**2)
        
        for i in range(0, len(self.arr)+1, 1):
            self.thread = self.threadExecutor.submit(self.bubbleSort_threadChunk, i, self.arr)

            logger.info("self.thread : {0}".format(self.thread))
            logger.warning("self.thread.result() == > {0}".format(self.thread.result()))
            
            self.arr = self.thread.result()[0]
            
            if not self.thread.result()[1]:
                break
            else:
                continue
            
        return self.arr
    def bubbleSort_threadChunk(self, i, n):
        swapped = False
        for j in range(0, len(n)-i-1, 1):
            if n[j] > n[j+1]:
                # Swap items
                n[j], n[j+1] = n[j+1], n[j]      
                swapped = True
                
        return [n, swapped]  

# Initialize class    
bubbleSort_ALGORITHM = bubbleSort()

pprint.pprint(
    bubbleSort_ALGORITHM.bubbleSort_withThreading(50),
    indent=100
)

bubbleSort_withThreading_TIMER = timeit.Timer("bubbleSort_ALGORITHM.bubbleSort_withThreading(5)", "from __main__ import bubbleSort_ALGORITHM")
bubbleSort_noThreading_TIMER = timeit.Timer("bubbleSort_ALGORITHM.bubbleSort_noThreading(5)", "from __main__ import bubbleSort_ALGORITHM")

for i in range(10):
    print()


repeat = eval(input("REPEAT > "))
pprint.pprint("BUBBLE SORT ALGORITHM WITH THREADING TIMING : {0}".format(bubbleSort_withThreading_TIMER.repeat(repeat=repeat, number=10000)), indent = 100)
pprint.pprint("BUBBLE SORT ALGORITHM NO THREADING TIMING : {0}".format(bubbleSort_noThreading_TIMER.timeit(repeat=repeat, number=10000)), indent = 100)
