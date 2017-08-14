=begin
Let d(n) be defined as the sum of proper divisors of n (numbers less than n
which divide evenly into n).
If d(a) = b and d(b) = a, where a ≠ b, then a and b are an amicable pair and
each of a and b are called amicable numbers.

For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55
and 110; therefore d(220) = 284. The proper divisors of 284 are 1, 2, 4, 71 and
142; so d(284) = 220.

Evaluate the sum of all the amicable numbers under 10000.
=end

def sum_of_factors(num)
    sum = 0
    (1..num-1).to_a.each do |x|
        if num % x == 0
            sum += x
        end
    end
    sum
end

def amicable?(num1, num2)
    sum_of_factors(num1) == num2 && sum_of_factors(num2) == num1 && num1 != num2
    end
#puts amicable?(220,284)
#puts amicable?(220, sum_of_factors(220))
#puts amicable?(10, sum_of_factors(10))

def amicable_numbers(max)
    sum = 0
    (1..max).to_a.each do |number|
        if amicable?(number, sum_of_factors(number))
            sum += number
        end
    end
    sum
end

#puts sum_of_factors(220)
#puts sum_of_factors(284)
puts amicable_numbers(10000)

