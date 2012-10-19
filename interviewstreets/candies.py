"""
Alice is a kindergarden teacher. She wants to give some candies to the children in her class.  
All the children sit in a line and each  of them  has a rating score according to his or her 
usual performance.  Alice wants to give at least 1 candy for each child.Children get jealous 
of their immediate neighbors, so if two children sit next to each other then the one with 
the higher rating must get more candies. Alice wants to save money, so she wants to minimize 
the total number of candies.
 
 
Input
 
The first line of the input is an integer N, the number of children in Alice's class. Each of 
the following N lines contains an integer indicates the rating of each child.
 
Ouput
 
Output a single line containing the minimum number of candies Alice must give.

"""


num_kids = int(raw_input())
ratings = []

for i in xrange(num_kids):
    ratings.append(int(raw_input()))

candies = [1 for i in xrange(num_kids)]
for i in xrange(1, num_kids):
	if ratings[i] > ratings[i-1]:
		candies[i] = candies[i-1] + 1


for i in xrange(num_kids - 2, -1, -1):
	if ratings[i] > ratings[i+1]:
		candies[i] = max(candies[i], candies[i+1] + 1)

print reduce(lambda x, y: x + y, candies)

