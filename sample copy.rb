def greet(name)
  "こんにちは、#{name}さん！"
end

def add(a, b)
  a + b
end

def fizzbuzz(n)
  (1..n).map do |i|
    if i % 15 == 0
      "FizzBuzz"
    elsif i % 3 == 0
      "Fizz"
    elsif i % 5 == 0
      "Buzz"
    else
      i.to_s
    end
  end
end

puts greet("エマ")
puts add(3, 7)
puts fizzbuzz(15).join(", ")
