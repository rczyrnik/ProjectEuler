#A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

#a2 + b2 = c2
#For example, 32 + 42 = 9 + 16 = 25 = 52.

#There exists exactly one Pythagorean triplet for which a + b + c = 1000.
#Find the product abc.

a = 1
b = 1
c = 1
sum = 1000
while a < sum:
	b=1
	while b < sum-a:
		c = sum-a-b
#		print "a, b, c, are:", a, b, c
		if a**2 + b**2 == c**2:
			print "Success!"
			print a, b, c
			print a*b*c
			break
		b += 1
	a += 1