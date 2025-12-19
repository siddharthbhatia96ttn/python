#Write a code using generator can be used to produce an infinite sequence of Fibonacci numbers
#Of 10  numbers 
def fibonacci():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

fib_gen = fibonacci()

for _ in range(10):
    print(next(fib_gen))



#2. Write a generator function called infinite_multiples(n) that yields multiples of the given base value indefinitely.
def infinite_multiples(n):
    multiple = 1
    while True:
        yield n * multiple
        multiple += 1

n = 3
gen = infinite_multiples(n)
for _ in range(10):
    print(next(gen))


#Write a generator function called repeat_word(word, times) that yields the given character char a specified number of times.
def repeat_word(word, times):
    for _ in range(times):
        yield word

gen = repeat_word("A", 5)

for value in gen:
    print(value)