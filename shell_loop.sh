#!/bin/sh

a=0
while [ "$a" -lt 20 ]    # pirmais cikls
do
   b="$a"
   while [ "$b" -ge 0 ]  # otrais cikls
   do
      echo -n "$b "
      b=`expr $b - 1`
   done
   echo
   a=`expr $a + 1`
done
