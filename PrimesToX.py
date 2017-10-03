def primes_to_x(x, frmt = "set"):
    if frmt == "list":
        p =[]
        with open("PrimesToTenMillion.txt") as f:
            data = f.read()
            for n in data.split():
                if int(n) > x:
                    return p
                p.append(int(n))
    elif frmt == "set":
        p = set()
        with open("PrimesToTenMillion.txt") as f:
            data = f.read()
            for n in data.split():
                if int(n) > x:
                    return p
                p.add(int(n))
    return False
