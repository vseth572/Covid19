import re
from collections import defaultdict, Counter
import random

my_regex = re.compile("[0-9]+", re.I)


def double(x): return x * 2


print(double(2))

### Exception Handling

try:
    print(0 / 0)
except ZeroDivisionError:
    print("cannot divide by zero")

### LIsts
l1 = [1, 2, 3, 4]
print(sum(l1))
print(l1[-1])
print(l1[-2])

## Get all the middle elements
print(l1[1:-1])

print(1 in l1)

## Extending lists
l2 = [3, 4, 5]
l1.extend(l2)
print(l1)
l1.append("xyz")
print(l1)

### Unpacking lists

x, y = [1, 23]

### Tuples - immuatble cousins of the lists

t = (1, 2, 3)


# t[1] = 4  #will give error
# returning multiple values f

def sum_and_product(x, y):
    return (x + y), (x * y)


print(sum_and_product(2, 4))

## Dictionaries
empty_dict = {}
grades = {"Joel": 80, "Tim": 95}
joel_grade = grades["Joel"]
print(joel_grade)

print(grades.get("Kate", 0))

grades["Kate"] = 100
print(len(grades))

print(grades.keys())  ## returns list of keys
print("Joel" in grades)

### Default dict

# word_counts = defaultdict(int)
# for word in document:
#     word_counts+=1

## Counter - it canbe primarily used to create histograms

c = Counter([0, 1, 2, 0])
print(c.most_common(1))

## Sets

s = set()
s.add(1)
s.add(2)
s.add(2)

## in has a very fast operation on sets

### Control Flow

x = 0
while x < 10:
    print(x, "is less than 10")
    x += 1

##Truthiness

print(x is None)
print(x is 0)
# print(x is NaN)

# use all to find if all the elments are truthy
# use any to find if any element is truthy
print(all([]))
print(any([2]))

## ADVANCED STUFF

# sorting
p = [4, 3, 2, 1]
b = sorted(p)
print(y)

## List comprehensions

even_numbers = [x for x in range(5) if x % 2 == 0]
print(even_numbers)
square_dict = {x: x * x for x in range(5)}
print(square_dict)

increasing_pairs = [(x, y) for x in range(10) for y in range(x + 1, 10)]
print(increasing_pairs)


## Generators and Iterators

def myyielder(n):
    for i in range(n):
        yield i


# print(myyielder(2))

##Random
random.seed(2)
print(random.randint(2, 5))
print(random.randint(2, 5))

## random sample
lottery_numbers = range(60)
winning_numbers = random.sample(lottery_numbers, 6)
print(winning_numbers)


## Map Reduce Filter

def double(x):
    return 2 * x


xs = [1, 2, 3, 4]
twice_xs = [double(x) for x in xs]
twice_xs = list(map(double, xs))
print(twice_xs)

def is_even(x):
    return x%2 == 0
x_evens = filter(is_even,xs)
print(list(x_evens))

### Enumerate

words = ["kite","doggo"]
for i,x in enumerate(words):
    print(i,x)

## ZIp and Argument Unpacking
print(list(zip([1,2,3],["abc","xyz","mno"])))

## Args and Kwargs

def magic(*args, **kwargs):
    print("unnamed args",args)
    print("kewwords args",kwargs)

magic(1,key = "word")


