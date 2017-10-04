'''
In the card game poker, a hand consists of five cards and are ranked,
from lowest to highest, in the following way:

High Card: Highest value card.
One Pair: Two cards of the same value.
Two Pairs: Two different pairs.
Three of a Kind: Three cards of the same value.
Straight: All cards are consecutive values.
Flush: All cards of the same suit.
Full House: Three of a kind and a pair.
Four of a Kind: Four cards of the same value.
Straight Flush: All cards are consecutive values of same suit.
Royal Flush: Ten, Jack, Queen, King, Ace, in same suit.
The cards are valued in the order:
2, 3, 4, 5, 6, 7, 8, 9, 10, Jack, Queen, King, Ace.

If two players have the same ranked hands
then the rank made up of the highest value wins;
for example, a pair of eights beats a pair of fives (see example 1 below).
But if two ranks tie, for example, both players have a pair of queens,
then highest cards in each hand are compared (see example 4 below);
if the highest cards tie then the next highest cards are compared, and so on.

Consider the following five hands dealt to two players:

Hand	 	Player 1	 	Player 2	 	Winner
1	 	5H 5C 6S 7S KD      2C 3S 8S 8D TD
        Pair of Fives       Pair of Eights  Player 2

(see https://projecteuler.net/problem=54 for the rest)

The file, poker.txt, contains one-thousand random hands dealt to two players.
Each line of the file contains ten cards (separated by a single space):
the first five are Player 1's cards and the last five are Player 2's cards.
You can assume that all hands are valid
(no invalid characters or repeated cards),
each player's hand is in no specific order,
and in each hand there is a clear winner.

How many hands does Player 1 win?
'''


def Straight(numbers):
    s = sorted(numbers)
    for n in range(0, 4):
        if s[n]+1 != s[n+1]: return False
    return True

def Flush(suits):
    for n in range(0, 4):
        if suits[n] != suits[n+1]: return False
    return True

def FourOfAKind(numbers):
    s = sorted(numbers)
    for n in range(0, 2):
        if s[n] == s[n+1] == s[n+2] == s[n+3]: return s[n]
    return False

def ThreeOfAKind(numbers):
    s = sorted(numbers)
    for n in range(0, len(s)-2):
        if s[n] == s[n+1] == s[n+2]: return s[n]
    return False

def Pair(numbers):
    s = sorted(numbers)
    for n in range(0, len(s)-1):
        if s[n] == s[n+1]: return s[n]
    return False

def best_hand(hand):
    # DEAL WITH NUMBERS
    numbers = [num_convert[n] for n in [hand[m] for m in range(0, 13, 3)]]

    # DEAL WITH SUITS
    suits = [hand[m] for m in range(1, 14, 3)]

    if Flush(suits):
        if Straight(numbers):
            if 13 in numbers:
                return 10               # ROYAL FLUSH
            else:
                return 9                # STRAIGHT FLUSH

    temp = FourOfAKind(numbers)
    if temp:
        return 8+temp/100               # FOUR OF A KIND

    temp = ThreeOfAKind(numbers)
    if ThreeOfAKind(numbers) and Pair([x for x in numbers if x != temp]):
        return 7+temp/100               # FULL HOUSE

    if Flush(suits):
        return 6 + max(numbers)/100     # FLUSH

    if Straight(numbers):
        return 5 + max(numbers)/100     # STRAIGHT

    temp = ThreeOfAKind(numbers)
    if temp:
        return 4 + temp/100             # THREE OF A KIND

    temp1 = Pair(numbers)
    if temp1:
        temp2 = Pair([x for x in numbers if x != temp1])
        if temp2:
            return 3 + temp1/100 + temp2/10000        # TWO PAIR
        else:
            return 2 + temp1/100 + max([x for x in numbers if x != temp1])/10000  # ONE PAIR

    return 1+ max(numbers) /100                # HIGH CARD


'''
1. High Card
2. One Pair: Two cards of the same value.
3. Two Pairs: Two different pairs.
4. Three of a Kind: Three cards of the same value.
5. Straight: All cards are consecutive values.
6. Flush: All cards of the same suit.
7. Full House: Three of a kind and a pair.
8. Four of a Kind: Four cards of the same value.
9. Straight Flush: All cards are consecutive values of same suit.
10. Royal Flush: Ten, Jack, Queen, King, Ace, in same suit.
'''

if __name__ == "__main__":
    num_convert = {'T':10, 'J':11, 'Q':12, 'K':13, 'A':14}
    for x in range(2, 10): num_convert[str(x)]=x

    wins = 0
    with open('E054.txt') as file:
        for hand in file.readlines():
            print()
            hand1 = hand[0:14]
            hand2 = hand[15:29]

            if best_hand(hand1) > best_hand(hand2):
                wins += 1
            elif best_hand(hand1) == best_hand(hand2):
                print("{}    {}".format(hand1, hand2))
                print("{0:.4f}              {1:.4f}".format(best_hand(hand1), best_hand(hand2)))
            # print()
    print(wins)


    # hand1 = '2H 2D 4C 4D 4S'
    # hand2 = '3C 3D 3S 9S 9D'
    # print("'{}', '{}'".format(hand1, hand2))
    # print("'{}', '{}'".format(best_hand(hand1), best_hand(hand2)))

    # numbers = [2, 2, 4, 4, 4]
    # temp = ThreeOfAKind(numbers)
    # print(temp)
    # print([x for x in numbers if x != temp])
    # print(Pair([x for x in numbers if x != temp]))
    # if ThreeOfAKind(numbers) and Pair([x for x in numbers if x != temp]):
    #     print(7+temp/100)              # FULL HOUSE
    #
    # print(Pair([1, 1]))

    # hand = '8C TS KC 9H 4S'
    #
    #
    # print(best_hand(hand))
    #
    # print(Straight([5,2,4,1,3]) == True)
    # print(Straight([5,2,8,1,3]) == False)
    # print()
    # print(Flush(['C','C','C','C','C']) == True)
    # print(Flush(['C','C','C','S','C']) == False)
    # print()
    # print(FourOfAKind([5,5,8,5,5]) == 5)
    # print(FourOfAKind([5,5,8,2,5]) == False)
    # print()
    # print(ThreeOfAKind([5,2,8,5,5]) == 5)
    # print(ThreeOfAKind([1,2,8,2,5]) == False)
    # print()
    # print(Pair([5,2,8,3,5]) == 5)
    # print(Pair([1,2,8,3,5]) == False)
