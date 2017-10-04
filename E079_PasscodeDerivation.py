'''
A common security method used for online banking
is to ask the user for three random characters from a passcode.
For example, if the passcode was 531278,
they may ask for the 2nd, 3rd, and 5th characters;
the expected reply would be: 317.

The text file, keylog.txt, contains fifty successful login attempts.

Given that the three characters are always asked for in order,
analyse the file so as to determine the shortest possible secret
passcode of unknown length.
'''
def check_num(short_str, long_str):
    short_pos = 0
    long_pos = 0
    for char in long_str:
        # print(char, short_str[short_pos], short_pos)
        if char == short_str[short_pos]:
            short_pos += 1
        if short_pos == 3:
            return True


    return False


if __name__ == "__main__":
    with open('E079.txt') as file:
        n = file.readlines()
    m = list(x.strip('\n') for x in n)

    guess = '73162890'
    # print(check_num('680',guess))
    for trial in m:
        print( trial, guess, check_num(trial, guess))
    #


    # guess = '37168290'
    # for trial in m:
    #     print( trial, guess, check_num(trial, guess))
    # print(check_num('123','123456') == True)
    # print(check_num('123','143456') == False)
    # print(check_num('123','122533456') == True)
