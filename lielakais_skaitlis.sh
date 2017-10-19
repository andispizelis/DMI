#!/bin/sh

echo -n "Ievadi 3 skaitlus (atdali katru ar atsarpi) : "
read a b c
# parbauda vai a>b un a>c
if [ $a -gt $b -a $a -gt $c ]
then
   big=$a
elif  [ $b -gt $a -a $b -gt $c ] # parbauda vai b>a un b>c
then
   big=$b
elif  [ $c -gt $a -a $c -gt $b ] # parbauda vai c>a un c>b
then
   big=$c
elif [ $a -eq $b -a $a -eq $c -a $b -eq $c -a $c -eq $b ] #parbauda vienadibu
then
   big="Visi skaitli ir vienadi"
else
   big="Nevar noteikt lielako skaitli"
fi
echo "Result : $big"
