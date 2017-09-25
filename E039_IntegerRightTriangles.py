'''
If p is the perimeter of a right angle triangle with integral length sides,
    {a,b,c}, there are exactly three solutions for p = 120.

{20,48,52}, {24,45,51}, {30,40,50}

For which value of p ≤ 1000, is the number of solutions maximised?
'''



def num_slns(p):
    max_c = int(.500 * p)  # p / 2
    min_c = int(.414 * p)  # p / (1+sqrt(2))
    max_b = int(.293 * p)  # p / (2+sqrt(2))

    num_slns = 0
    for c in range(int(min_c), int(max_c)):
        for b in range(1, int(max_b)):
            a = p - b - c
            if a**2 + b**2 == c**2:
                num_slns += 1
    return num_slns


if __name__ == "__main__":

    max_slns = 0
    max_p = 0

    for p in range(3, 1001):
        ns = num_slns(p)
        print(p, ns)
        if ns > max_slns:
            max_slns = ns
            max_p = p
    print(max_slns, max_p)
