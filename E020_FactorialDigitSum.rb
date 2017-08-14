
=begin
n! means n × (n − 1) × ... × 3 × 2 × 1

For example, 10! = 10 × 9 × ... × 3 × 2 × 1 = 3628800,
and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.

Find the sum of the digits in the number 100!
=end

def factorial_digit_sum(num)
    product = 1
    (1..num).to_a.each {|num| product *= num}

    sum = 0
    product.to_s.chars.each {|num| sum += num.to_i}

    return sum
end

puts factorial_digit_sum(100)
