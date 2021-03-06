'''
Triangle, pentagonal, and hexagonal numbers are generated by the following formulae:

Triangle	 	Tn=n(n+1)/2	 	1, 3, 6, 10, 15, ...
Pentagonal	 	Pn=n(3n−1)/2	 1, 5, 12, 22, 35, ...
Hexagonal	 	Hn=n(2n−1)	 	1, 6, 15, 28, 45, ...
It can be verified that T285 = P165 = H143 = 40755.

Find the next triangle number that is also pentagonal and hexagonal.
'''


if __name__ == "__main__":
    tri = set()
    penta = set()
    hexa = set()

    for n in range(1, 10000000):

        h = n*(2*n-1)
        hexa.add(h)

        p = (n*(3*n-1))//2
        if p in hexa:
            penta.add(p)

        t = n*(n+1)//2
        if t in penta:
            tri.add(t)

    # print(hexa)
    # print(penta)
    print(tri)
