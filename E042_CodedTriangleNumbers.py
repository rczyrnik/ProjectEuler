'''
The nth term of the sequence of triangle numbers is given by, tn = ½n(n+1);
so the first ten triangle numbers are:

1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...

By converting each letter in a word to a number corresponding to its
alphabetical position and adding these values we form a word value.
For example, the word value for SKY is 19 + 11 + 25 = 55 = t10.
If the word value is a triangle number then we shall call the word a triangle word.

Using words.txt (right click and 'Save Link/Target As...'),
a 16K text file containing nearly two-thousand common English words,
how many are triangle words?
'''

def alphabet_value(word):
    sum = 0
    for letter in word:
        sum += decode[letter]
    return sum


if __name__ == "__main__":

    decode = dict( (chr(k), v) for (k, v) in zip( range(ord('A'),ord('Z')+1), range(1,27) ) )

    triangle = [n*(n+1)//2 for n in range(0, 45)]

    count = 0

    with open("E042_words.txt") as f:
        data = f.read()

    for x in data.split(','):
        if alphabet_value(x.strip('"')) in triangle:
        # if alphabet_value(x.strip('"')) is in triangle:
            count += 1
    # words = [x.strip('"') for x in data.split(',')]
    print(count)
