#!/bin/bash
clear
for i in {1..100000}
do
   echo "Corriendo $i veces"
   python a.py
   sleep 3
done


