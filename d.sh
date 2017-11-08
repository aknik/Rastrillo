#!/bin/bash
clear
for i in {1..100000}
do
   echo "Corriendo $i veces"
   python b.py
   sleep 3
done


