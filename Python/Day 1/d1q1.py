"""" Day 1: Question 1 of Advent of Code 2024 """

list1 = []
list2 = []

with open('input.txt', 'r', encoding='utf-8') as file:
    for line in file:
        num1, num2 = line.split()
        list1.append(int(num1))
        list2.append(int(num2))

list1.sort()
list2.sort()

total_distance = sum(abs(a - b) for a, b in zip(list1, list2))

print("Total distance:", total_distance)
