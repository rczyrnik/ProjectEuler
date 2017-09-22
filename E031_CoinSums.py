'''
In England the currency is made up of pound, £, and pence, p, and there are eight coins in general circulation:

1p, 2p, 5p, 10p, 20p, 50p, £1 (100p) and £2 (200p).
It is possible to make £2 in the following way:

1×£1 + 1×50p + 2×20p + 1×5p + 1×2p + 3×1p
How many different ways can £2 be made using any number of coins?
'''

if __name__ == "__main__":
    #coins = [2, 5, 10, 20, 50, 100, 200]
    coins = [200, 100]
    purse = {}

    for coin in coins:
        purse[coin] = 200/coin
    # print(purse)



    count = 0
    for num_200 in range(0, 200/200+1):
        for num_100 in range(0, 200/100+1):
            for num_50 in range(0,200/50+1):
                for num_20 in range(0, 200/20+1):
                    for num_10 in range(0, 200/10+1):
                        for num_5 in range(0, 200/5+1):
                            for num_2 in range(0, 200/2+1):
                                remaining = 200-200*num_200-100*num_100-50*num_50-20*num_20-10*num_10-5*num_5-2*num_2
                                if remaining > -1:
                                    # print("{} $2 coins and".format(num_200))
                                    # print("{} $1 coins and".format(num_100))
                                    # print("{} 50c coins".format(num_50))
                                    # print("leaves {} remaining".format(remaining))
                                    # print('')
                                    count += 1
    print("{} ways of making $2 with the coins".format(count))
