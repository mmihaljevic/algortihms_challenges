"""
There are many duplicates in the lists, but you need to find the extra numbers, 
i.e. B - A. Print the numbers in numerical order. Print each missing number 
once, even if it is missing multiple times. The numbers are all within a 
range of 100 from each other.
"""
n = input()
l1 = raw_input().strip().split()

m = input()
l2 = raw_input().strip().split()

d = {}

if m < n:
    first = n
    second = m
    list1 = l1
    list2 = l2

else:
    first = m
    second = n
    list1 = l2
    list2 = l1

for i in xrange(first):
    if d.has_key(list1[i]):
        d[list1[i]] += 1
    else:
        d[list1[i]] = 1
for i in xrange(second):
    if d.has_key(list2[i]):
        if d[list2[i]] > 1:
            d[list2[i]] -= 1
        else:
            del(d[list2[i]])

result = sorted(d.keys())
print " ".join(result)

