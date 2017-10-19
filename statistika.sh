#!/bin/sh
if [ $# == 3 ]
then
if [ $a -gt $b -a $a -gt $c ]
then
   max=$a
elif  [ $b -gt $a -a $b -gt $c ] # parbauda vai b>a un b>c
then
   max=$b
elif  [ $c -gt $a -a $c -gt $b ] # parbauda vai c>a un c>b
then
   max=$c
elif [ $a -eq $b -a $a -eq $c -a $b -eq $c -a $c -eq $b ] #parbauda vienadibu
then
   max="Visi skaitli ir vienadi"
else
   max="Nevar noteikt lielako skaitli"
fi
echo "Result : $max"
fi
