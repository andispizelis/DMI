#!/bin/bash

declare nos[5]=(4 -1 2 66 10)


echo "Originali skaitli masiva:"
for (( i = 0; i <= 4; i++ ))
    do
      echo ${nos[$i]}
    done



for (( i = 0; i <= 4 ; i++ ))
do
   for (( j = $i; j <= 4; j++ ))
   do
      if [ ${nos[$i]} -gt ${nos[$j]}  ]; then
       t=${nos[$i]}
       nos[$i]=${nos[$j]}
       nos[$j]=$t
      fi
   done
done
 
echo -e "\n Skaitli augosa seciba:"
for (( i=0; i <= 4; i++ )) 
do
  echo ${nos[$i]}
done
