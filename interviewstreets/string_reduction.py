"""
Given a string consisting of a,b and c's, we can perform the following operation: Take any two adjacent distinct characters and replace it with the third character. For example, if 'a' and 'c' are adjacent, they can replaced with 'b'. What is the smallest string which can result by applying this operation repeatedly?

Input:
The first line contains the number of test cases T. T test cases follow. Each case contains the string you start with.

Output:
Output T lines, one for each test case containing the smallest length of the resultant string after applying the operations optimally.

Constraints:
1 <= T <= 100
The string will have at most 100 characters.

Sample Input:
3
cab
bcab
ccccc

Sample Output:
2
1
5


"""

value = 1
minimum = 1

def change(reduce):
    val = 'b';
    if reduce == "bc" or reduce == "cb":
        val = 'a';
    elif reduce == "ab" or reduce == "ba":
        val = 'c';
    return val
    

def reduce(string):
    global value
    global minimum
    minimum = len(string)
    length = len(string)

    if length == 1:
        value = 1
        return True
    elif string[0] == string[1] and length == 2:
        value = 2
        return True
    for i in xrange(len(string)-1):
        if string[i+1]!=string[i]:
            red = string[i+1] + string[i]
            r = change(red)
            sub1 = ""
            sub2 = r
            sub3 = ""
            if i==1:
                sub1= string[0]
            elif i > 1:
                sub1 = string[0:i]
            if i+2 < length - 1 :
                sub3 = string[i+2:]
            elif i+2 == length - 1 :
                sub3 = string[i+2]
            cat = sub1 + sub2 + sub3
            #print cat
            flag = reduce(cat)
            #print flag
            if(flag):
                minimum = min(minimum, value);
                return flag
    return False      

num_cases = int(raw_input())

for i in xrange(0,num_cases):
    string = raw_input()
    reduce(string)
    print minimum
