#!/bin/bash

mkdir build
cd build
cmake .. -Dtest=on
make -j8
clear
ctest --verbose
cd ..
rm -rf build