#!/bin/bash
c=0
a=1
b=1
read -p "Ievadi skaitli:" n
echo -n "$a "
echo -n "$b "
#Fibonacci virknes algortims
while((c<n)) 
do
c=$((a+b))
echo -n "$c "
a=$b
b=$c
done
echo -e "\n"
