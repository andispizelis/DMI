#!/bin/bash
d=y
c=0
a=1
b=1
read -p  "Sveiks,vai velies sakt algoritmu?(y/n)" 
echo  "$d "
if [   $d == y ]
then

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
else
echo "Nu varbut citreiz!"
fi
