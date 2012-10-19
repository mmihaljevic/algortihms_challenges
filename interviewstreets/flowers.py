# You and your K-1 friends want to buy N flowers. Flower number i has host ci. 
# Unfortunately the seller does not like a customer to buy a lot of flowers, 
# so he tries to change the price of flowers for customer who had bought flowers before. 
# More precisely if a customer has already bought x flowers, he should pay (x+1)*ci dollars to buy flower number i.
# You and your K-1 firends want to buy all N flowers in such a way that you spend the as few money as possible.

# Input:

# The first line of input contains two integers N and K.
# next line contains N positive integers c1,c2,...,cN respectively.

# Output:

# Print the minimum amount of money you (and your friends) have to pay in order to buy all n flowers.

N,K = raw_input().split()
flowers = int(N)
friends = int(K)

C = raw_input().split()
c = [int(i) for i in C]
costs = sorted(c)

count = 0
cost = 0
factor = 0

index = len(costs) - 1
while count != flowers:
	if count % friends == 0:
		factor += 1
	cost = cost + (costs[index] * factor);
	index -= 1
	count += 1

print cost
