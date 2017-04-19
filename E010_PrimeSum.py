#The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

#Find the sum of all the primes below two million.

below = 2000000

sum = 2
i=3
primes=[2]while i < below:    is_prime=True    for num in primes:        if num > i**.5:
		break
	elif i % num == 0:            is_prime = False
	    break    if is_prime == True:        primes.insert(len(primes), i)
	sum += i    i +=2print sum