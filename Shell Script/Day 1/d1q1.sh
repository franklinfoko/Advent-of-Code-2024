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

total_distance=0
for i in "${!list1[@]}"; do
    diff=$((list1[i] - list2[i]))
    abs_diff=${diff#-}
    total_distance=$((total_distance + abs_diff))
done

echo "Total distance: $total_distance"