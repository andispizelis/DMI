#!/bin/sh

if [ $# == 2 ]
then

#a=0
#b=-36

if [ $a -eq $b ] #parbauda  vienadibu
then
   echo "$a -eq $b : a is equal to b" # patiesa
else
   echo "$a -eq $b: a is not equal to b" #aplama
fi

if [ $a -ne $b ] #vienadibas parbaude
then
   echo "$a -ne $b: a is not equal to b" #patiesa
	else
   echo "$a -ne $b : a is equal to b" #aplama
fi

if [ $a -gt $b ] #parbauda vai pirma vertiba ir lielaka par otro
then
   echo "$a -gt $b: a is greater than b" # patiesa
else
   echo "$a -gt $b: a is not greater than b" #aplama
fi

if [ $a -lt $b ] #parbauda vai pirma vertiba ir mazaka par otro
then
   echo "$a -lt $b: a is less than b" #patiesa
else
   echo "$a -lt $b: a is not less than b" #aplama
fi

if [ $a -ge $b ] #parbauda vai pirmaa vertiba ir lielaka vai vienada ar otro
then
   echo "$a -ge $b: a is greater or  equal to b" #patiesa
else
   echo "$a -ge $b: a is not greater or equal to b" #aplama
fi

if [ $a -le $b ]  # parbauda vai pirma vetiba ir mazaka vai vienada par otro
then
   echo "$a -le $b: a is less or  equal to b" #patiesa
else
   echo "$a -le $b: a is not less or equal to b" # aplama
fi
fi

