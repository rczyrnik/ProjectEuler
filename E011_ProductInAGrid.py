

with open('E011.txt') as f:
    a = []
    for line in f: # read rest of lines
        a.append([int(x) for x in line.split()])

product = 0
#test rows
i = 0
while i < 20:
	j = 0
	while j < 17:
		prod= a[i][j]*a[i][j+1]*a[i][j+2]*a[i][j+3]
		if product < prod:
			product = prod
		j +=1
	i +=1
print product

#test columns
i = 0
while i < 17:
	j = 0
	while j < 20:
		prod= a[i][j]*a[i+1][j]*a[i+2][j]*a[i+3][j]
		if product < prod:
			product = prod
		j +=1
	i +=1
print product

#test diagonals 1
i = 0
while i < 17:
	j = 0
	while j < 17:
		prod= a[i][j]*a[i+1][j+1]*a[i+2][j+2]*a[i+3][j+3]
		if product < prod:
			product = prod
		j +=1
	i +=1
print product

#test diagonals 2
i = 0
while i < 17:
	j = 19
	while j >= 0:
		prod= a[i][j]*a[i+1][j-1]*a[i+2][j-2]*a[i+3][j-3]
		if product < prod:
			product = prod
		j -=1
	i +=1
print product