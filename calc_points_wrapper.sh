#!/bin/bash

for file in `find . -wholename "*_pregledano/kljuc.txt"`; do
    echo ${file:2:8}
    ./calc_points.py $file
done
