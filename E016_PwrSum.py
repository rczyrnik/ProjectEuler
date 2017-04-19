#215 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.

#What is the sum of the digits of the number 21000?



with open('E016_PwrSum.txt') as f:
	n = 5
	sum = 0
	while n <= 306:
		num = f.read(1)
		print num
		sum += int(num)
		n +=1

print "The sum is " + str(sum)