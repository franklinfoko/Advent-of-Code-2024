"""" Day 1: Question 2 of Advent of Code 2024 """
from collections import Counter

list1 = []
list2 = []

with open('input.txt', 'r', encoding='utf-8') as file:
    for line in file:
        num1, num2 = line.split()
        list1.append(int(num1))
        list2.append(int(num2))

list1.sort()
list2.sort()
count_list2 = Counter(list2)

total_similarity_score = sum(num * count_list2[num] for num in list1)

print("Total similarity score:", total_similarity_score)
