
gnuplot -e '
  set key outside;
  set xrange[0:40];
  set yrange[-0.1:];
  set xlabel "time(sec)";
  set ylabel "(m)";
  plot "plot-x.dat" using 1:2 title "x" w l lw 3 lc rgb "red";
  replot "plot-y.dat" using 1:2 title "y" w l lw 3 lc rgb "blue";
  replot "plot-z.dat" using 1:2 title "z" w l lw 3 lc rgb "green";
  set term png;
  set output "plot_trajectory.png";
  rep;
'
