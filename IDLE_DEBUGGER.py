def mergeSort(arr):
    if len(arr) > 1:
        # Split array in half and merge sort each half
        middle = len(arr) // 2

        L = arr[middle:]
        R = arr[:middle]

        # Merge sort each half
        mergeSort(L)
        mergeSort(R)

        i = j = k = 0
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                # Add L[i] to arr[k]
                arr[k] = L[i]
                
                # Increment vars
                i += 1
                k += 1
            else:
                # Add R[j] to arr[k]
                arr[k] = R[j]

                # Increment vars
                j += 1
                k += 1


        # Add left over values to | arr | array
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1
        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1
            
RANGE_STOP = eval(input("RANGE STOP > "))
n = list(range(1, RANGE_STOP+1, 1))[::-1]
print("Array before merge sort : {0}".format(n))
mergeSort(n)
print("Array after merge sort : {0}".format(n))
