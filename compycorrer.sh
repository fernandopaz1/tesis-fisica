#!/bin/bash
reset
file=main
# gcc -O3 -W $file.cpp -o $file.e -lm

g++ -o $file.e $file.cpp -Ofast -lboost_iostreams -lboost_system -lboost_filesystem
./$file.e
rm $file.e
