#If the numbers 1 to 5 are written out in words=> one, two, three, four, five, then there #are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.
#
#If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how #many letters would be used?
#
#
#NOTE=> Do not count spaces or hyphens. For example, 342 (three hundred and forty-two) #contains 23 letters and 115 (one hundred and fifteen) contains 20 letters. The use of #"and" when writing out numbers is in compliance with British usage.

=begin
1 to 9=> 6+16+14 = 6+30 = 36					TOTAL=> 36
0 zero  -
1 one	3
2 two	3
3 three	5
4 four	4
5 five	4
6 six	3
7 seven	5
8 eight	5
9 nine	4                                   

10 to 19=> 15+15+15+17+8 = 45+25 = 70		TOTAL=> 36+70 = 106
10	ten			3
11	eleven		6
12	twelve		6
13	thirteen	8
14	fourteen	8
15	fifteen		7
16	sixteen		7
17	seventeen	9
18	eighteen	8
19	nineteen	8

20 to 100=> 12+15+19 = 27+19 = 46			TOTAL=> = 106+460+700 = 1266
20 	twenty	6
30 	thirty	6
40	forty	5
50	fifty	5
60	sixty	5
70	seventy	7
80	eighty	6
90	ninety	6

100
200
300
400
500
600
700
800
900
1000

=end


def small_word_to_num(number)
    ones = {0=>0, 1=>3, 2=>3, 3=>5, 4=>4, 5=>4, 6=>3, 7=>5, 8=>5, 9=>4, 10=>3, 11=>3, 12=>6, 13=>8, 14=>8, 15=>7, 16=>7, 17=>9, 18=>8, 19=>8}
    tens = {0=>0, 1=>0, 2=>6, 3=>6, 4=>5, 5=>5, 6=>5, 7=>7, 8=>6, 9=>6}
    

    count = 0

    if number < 20
        return ones[number]
    else number < 99
        return tens[number/10] + ones[number%10]
    end

end

def large_word_to_num(number)
    ones = {0=>0, 1=>3, 2=>3, 3=>5, 4=>4, 5=>4, 6=>3, 7=>5, 8=>5, 9=>4, 10=>3, 11=>3, 12=>6, 13=>8, 14=>8, 15=>7, 16=>7, 17=>9, 18=>8, 19=>8}
    tens = {0=>0, 1=>0, 2=>6, 3=>6, 4=>5, 5=>5, 6=>5, 7=>7, 8=>6, 9=>6}

    if number < 100
        return small_word_to_num(number)
    elsif number < 1000
        if number%100 == 0
            return ones[number/100]+7
        else
            return ones[number/100]+10+small_word_to_num(number%100)
        end
    elsif number == 1000
        return 11
    else
        return 0
    end
end


puts large_word_to_num(9)
puts large_word_to_num(20)
puts large_word_to_num(27)
puts large_word_to_num(109)
puts large_word_to_num(100)
puts large_word_to_num(1000)

def how_many_char(max)

    num_char = 0
    count = 1

    while count <= max
        num_char += large_word_to_num(count)
        count += 1
    end

    num_char
end

puts how_many_char(1000)

