#!/bin/bash
clear


for i in {1..5}
do
   echo "Corriendo $i veces"
   sleep 2
   python rastrillo.py
done

