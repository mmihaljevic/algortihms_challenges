"""
Given a sorted list with an unsorted number V in the right-most cell, 
can you write some simple code to insert V into the array so it remains sorted?

Print the array every time a value is shifted in the array until the array 
is fully sorted. The goal of this challenge is to follow the correct order 
of insertion sort.
"""
# Head ends here
def insertionSort(ar):    
    i = len(ar) - 2
    element = ar[i+1]
    while i >= 0 and element < ar[i]:
        ar[i+1] = ar[i]
        p = [str(j) for j  in ar]
        print " ".join(p)
        i -= 1
    ar[i+1] = element
    p = [str(i) for i in ar]
    print " ".join(p)

    # Tail starts here

m = raw_input()
ar = [int(i) for i in raw_input().strip().split()]
insertionSort(ar)
