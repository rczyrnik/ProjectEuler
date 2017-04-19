n = int(raw_input("How wide is an edge?"))
#n=4
m = (n-1)*2
#m = 6

i = 0
numerator = 1
x = n
#x = 4
while i < n-1:
	numerator = numerator*x
	i +=1
	x +=1

#i = 0 --> num = 1*(4) = 4
#i = 1 --> num = 4*(5) = 20
#i = 2 --> num = 20*(6) = 120
#i = 3 STOP

j = 0
denominator = 1
y = n-1
#y = 3
while j < n-2:
	denominator = denominator*y
	j +=1
	y -=1

#j = 0 --> denom = 1(3) = 3
#j = 1 --> denom = 3(2) = 6
#j = 2 STOP

print "The numerator is " + str(numerator)
print "The denominator is " + str(denominator)
ans = numerator/denominator
print "The answer is " + str(ans)


