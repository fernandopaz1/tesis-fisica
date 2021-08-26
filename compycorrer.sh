#!/bin/bash
reset
file=main
gcc -O3 -W $file.c -o $file.e -lm
./$file.e