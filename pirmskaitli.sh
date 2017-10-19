#!/bin/sh
i=3
j=100
a=0
b=2
echo "1"
while [ $i -ne $j  ]
do
temp=`echo $i`
while [ $temp -ne $b ]
do
temp=`expr $temp - 1`
n=`expr $i % $temp`
if [ $n -eq 0 -a $a -eq 0  ]
then
a=1
fi
done
if [ $a -eq 0 ]
then
echo $i
else
a=0
fi
i=`expr $i + 1`
done
