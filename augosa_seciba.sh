#!/bin/sh
declare nos[5]= ( 4 -1 2 66 10 )
echo "Originalie skaitli masiva"
for (( i = 0; i <= 4; i++ ))
do 
echo ${nos[$i]}
done
for (( i = 0; i <= 4; i++ ))
do
for (( j = $i; j <=4; j++ ))
do
if [ ${nos[$i]} -gt ${nos[j]}
t=${nos[$i]}
nos[$i]=${nos[j]}
nos[$j]=$t
fi
done
done
echo -e "\n Sakartoti augosa seciba"
for (( i = 0; i <= 4; i++ ))
do
echo ${nos[$i]}
done
