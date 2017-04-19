
Greatest = 0
Starting = 0
i = 3
while i < 1000000:
	n = i
	length = 0
	while n != 1:
		if n % 2 == 0:
			n = n/2
		else:
			n = 3*n+1
		length +=1
	if length > Greatest:
		Greatest = length
		Starting = i
	i+=2


print "The greatest length starts at " + str(Starting)
