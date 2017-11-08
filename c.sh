#!/bin/bash
clear
for i in {1..100000}
do
   echo "Corriendo $i veces"
   python c.py
   sleep 3
done


