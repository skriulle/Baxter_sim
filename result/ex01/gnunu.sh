
gnuplot -e '
  set key outside;
  set term png enh;
  set output "plot_torque.png";
  set yrange[:40];
  set xlabel "time(sec)";
  set ylabel "  (Nm)";
  plot "plot01.dat" using 1:2 title "1" w l lw 3;
  replot "plot02.dat" using 1:2 title "2" w l lw 3;
  replot "plot03.dat" using 1:2 title "3" w l lw 3;
  replot "plot04.dat" using 1:2 title "4" w l lw 3;
  replot "plot05.dat" using 1:2 title "5" w l lw 3;
  replot "plot06.dat" using 1:2 title "6" w l lw 3;
  replot "plot07.dat" using 1:2 title "7" w l lw 3;
  rep;
  set term png;
  set output "plot_torque.png";
  rep;
'
