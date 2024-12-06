#!/bin/bash

list1=()
list2=()

while read -r line; do
    num1=$(echo $line | awk '{print $1}')
    num2=$(echo $line | awk '{print $2}')

    list1+=($num1)
    list2+=($num2)
done < input.txt

# sort the lists
list1=($(echo ${list1[@]} | tr ' ' '\n' | sort -n | tr '\n' ' '))
list2=($(echo ${list2[@]} | tr ' ' '\n' | sort -n | tr '\n' ' '))


declare -A count_list2
for num in "${list2[@]}"; do
    count_list2[$num]=$((count_list2[$num] + 1))
done

total_distance=0
for num in "${list1[@]}"; do
    count=${count_list2[$num]:-0}
    total_similarity_score=$((total_similarity_score + num * count))
done

echo "Total similarity score: $total_similarity_score"
