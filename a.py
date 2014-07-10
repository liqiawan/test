def func(x):
	return sum(range(1,x+1))**2 - sum([i**2 for i in range(1,x+1)])

print func(100)

for i in range(1,10):
	if i==5:
		print "hit"
