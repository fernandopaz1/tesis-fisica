#!/usr/bin/gnuplot
set datafile separator ","
set terminal pdf
set output 'output.pdf'
set autoscale yfix
set autoscale xfix
set palette defined (0 0 0 0.5, 1 0 0 1, 2 0 0.5 1, 3 0 1 1, 4 0.5 1 0.5, 5 1 1 0, 6 1 0.5 0, 7 1 0 0, 8 0.5 0 0)
set pm3d map
splot 'topologyDataActive' matrix with image notitle 
pause 1; refresh; reread;

# # Set the output to a png file
# set terminal png size 500,500
# # The file we'll write to
# set output 'sinx.png'
# # The graphic title
# set title 'Sin(x)'
# #plot the graphic
# plot sin(x)