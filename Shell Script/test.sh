#!/bin/bash

# Définir la liste
list2=("apple" "banana" "apple" "orange" "banana" "apple")

# Compter les occurrences de chaque élément et formater en dictionnaire
echo "${list2[@]}" | tr ' ' '\n' | sort | uniq -c | awk 'BEGIN { print "{" } { printf "\"%s\": %s", $2, $1; if (NR != NF) printf ", " } END { print "}" }'