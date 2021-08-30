#!/bin/bash
reset
file=main
# gcc -O3 -W $file.cpp -o $file.e -lm

g++ -o main.e main.cpp -lboost_iostreams -lboost_system -lboost_filesystem
./$file.e