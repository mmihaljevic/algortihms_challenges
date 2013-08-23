"""
In this challenge, don't print every time you move an element. 
Instead, print the array every time an element is "inserted" into the 
array in (what is currently) its correct place. Since the first 
element is already "sorted", begin printing from the second element and on.

6
1 4 3 5 6 2

1 4 3 5 6 2 
1 3 4 5 6 2 
1 3 4 5 6 2 
1 3 4 5 6 2 
1 2 3 4 5 6 
"""


def insertionSort(ar):  
    for i in xrange(1,len(ar)):
        j = i-1
        element = ar[i]
        while j >= 0 and element < ar[j]:
            ar[j+1] = ar[j]
            j -= 1
        ar[j+1] = element
        p = [str(j) for j in ar]
        print " ".join(p)

 
m = raw_input()
ar = [int(i) for i in raw_input().strip().split()]
insertionSort(ar)



