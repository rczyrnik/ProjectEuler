=begin
By starting at the top of the triangle below and moving to adjacent numbers on
the row below, the maximum total from top to bottom is 23.

3
7 4
2 4 6
8 5 9 3

That is, 3 + 7 + 4 + 9 = 23.

Find the maximum total from top to bottom of the triangle below:

75
95 64
17 47 82
18 35 87 10
20 04 82 47 65
19 01 23 75 03 34
88 02 77 73 07 63 67
99 65 04 28 06 16 70 92
41 41 26 56 83 40 80 70 33
41 48 72 33 47 32 37 16 94 29
53 71 44 65 25 43 91 52 97 51 14
70 11 33 28 77 73 17 78 39 68 17 57
91 71 52 38 17 14 91 43 58 50 27 29 48
63 66 04 68 89 53 67 30 73 16 69 87 40 31
04 62 98 27 23 09 70 98 73 93 38 53 60 04 23

NOTE: As there are only 16384 routes, it is possible to solve this problem by
trying every route. However, Problem 67, is the same challenge with a triangle
containing one-hundred rows; it cannot be solved by brute force, and requires a
clever method! ;o)
=end

def maximum_path_sum()

pyramid = File.open("p067_triangle.txt").read
pyramid = pyramid.split"\n"

pyramid.each_with_index do |line, i|
    line = line.split
    line.each_index {|i| line[i] = line[i].to_i}
    pyramid[i] = line
    end

line_no = pyramid.length-1


while line_no >= 0
    y = 0
    this_line = pyramid[line_no]
    next_line = pyramid[line_no-1]
    while y < this_line.length-1
        if this_line[y] > this_line[y+1]
            next_line[y] = next_line[y]+this_line[y]
        else
            next_line[y] = next_line[y]+this_line[y+1]
        end
        y += 1
    end
    line_no -= 1
end

puts pyramid[0]

end

maximum_path_sum()
