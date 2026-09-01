roll_no = "1024170191"

L = [int(digit) * 10 for digit in roll_no]

# print(L)

# L.append(110)

# print(L)

# L.insert(2,50)

# print(L)

# L.remove(50)

# print(L)

# L.pop(0)

# print(L)

# L.sort()

# print(L)

# L.sort(reverse=True)

# print(L)

# print(L[:3])

# print(L[-3:])

# average = sum(L) / len(L)

# greater_than_average = [x for x in L if x > average]

# print(greater_than_average)


#question 2

scores = tuple(L[0:8])
print("Scores:", scores)

highest = max(scores)
print("Highest score:", highest)
print("Index:", scores.index(highest))

lowest = min(scores)
print("Lowest score:", lowest)
print("Count:", scores.count(lowest))

rev_list = list(scores[::-1])
print("Reversed list:", rev_list)

x = int(input("Enter a score: "))

if x in scores:
    print("First occurrence index:", scores.index(x))
else:
    print("Score is not present")

scores[0] = 100

first_score, second_score, *remaining_scores = scores

print("First score:", first_score)
print("Second score:", second_score)
print("Remaining scores:", remaining_scores)

#question 3
import random

random.seed(roll_no)

numbers = []

for i in range(100):
    numbers.append(random.randint(100, 900))

odd = 0
even = 0
prime = 0
prime_numbers = []

for n in numbers:
    if n % 2 != 0:
        odd += 1
    else:
        even += 1

    is_prime = True

    if n < 2:
        is_prime = False

    for i in range(2, n):
        if n % i == 0:
            is_prime = False
            break

    if is_prime:
        prime += 1
        prime_numbers.append(n)

print("Odd numbers:", odd)
print("Even numbers:", even)
print("Prime numbers:", prime)
print("Prime list:", prime_numbers)

most = numbers[0]
count = numbers.count(most)

for n in numbers:
    if numbers.count(n) > count:
        most = n
        count = numbers.count(n)

print("Most frequent number:", most)
print("Number of times:", count)


#q4
import random

random.seed(roll_no)

numbers = []

for i in range(100):
    numbers.append(random.randint(100, 900))

odd = 0
even = 0
prime = 0
prime_numbers = []

for n in numbers:
    if n % 2 != 0:
        odd += 1
    else:
        even += 1

    is_prime = True

    if n < 2:
        is_prime = False

    for i in range(2, n):
        if n % i == 0:
            is_prime = False
            break

    if is_prime:
        prime += 1
        prime_numbers.append(n)

print("Odd numbers:", odd)
print("Even numbers:", even)
print("Prime numbers:", prime)
print("Prime list:", prime_numbers)

most = numbers[0]
count = numbers.count(most)

for n in numbers:
    if numbers.count(n) > count:
        most = n
        count = numbers.count(n)

print("Most frequent number:", most)
print("Number of times:", count)

#q5
my_dict = {
    "name": "Ashwin Garg",
    "roll_no": "1024170191",
    "branch": "CSE",
    "age": 20,
    "city": "Bathinda"
}

location = my_dict.pop("city")
my_dict["location"] = location
print(my_dict)

my_dict["cgpa"] = 8.5
print(my_dict)

my_dict["age"] = my_dict["age"] + 1
print(my_dict)

dict1 = my_dict.copy()
dict2 = my_dict.copy()

branch1 = dict1.pop("branch")
del dict2["branch"]

print(dict1)
print(dict2)

for key, value in my_dict.items():
    print(key, "→", value)

if "email" in my_dict:
    print(my_dict["email"])
else:
    print("Email is not present")

friend_dict = {
    "name": "Rahul Sharma",
    "roll_no": "1024170192",
    "branch": "CSE",
    "age": 21,
    "city": "Amritsar"
}

merged_dict = {**my_dict, **friend_dict}
print(merged_dict)

string_dict = {key: value for key, value in my_dict.items() if type(value) == str}
print(string_dict)