


test_cases = input()

for test in xrange(test_cases):

    n, k = raw_input().strip().split()
    n = int(n)
    k = int(k)



    arr1 = raw_input().split()
    arr1 = [int(i) for i in arr1]

    arr2 = raw_input().split()
    arr2 = [int(i) for i in arr2]

    arr1.sort()
    arr2.sort(reverse=True)
    result = True
    for i in xrange(n):
        if arr1[i] + arr2[i] < k:
            print "NO"
            result = False
            break
    if result:
        print "YES"



