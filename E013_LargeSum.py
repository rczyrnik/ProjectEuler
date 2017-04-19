#Work out the first ten digits of the sum of the following one-hundred 50-digit numbers.


# XXX
#  XXX
#   XXX
#    XXX

with open('E013.txt') as f:
    a = []
    for line in f: # read rest of lines
        a.append([int(x) for x in line.split()])

BigSum = 0
j = 1
while j < 13:
	i = 0
	SmallSum = 0
	while i < len(a):
		b = str(a[i])
		SmallSum += int(b[j])
		i += 1
	print SmallSum
	BigSum += SmallSum*10**(10-j)
	print BigSum
	j += 1


