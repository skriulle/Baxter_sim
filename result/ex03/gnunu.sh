
gnuplot -e '
  plot "plot01.dat" using 1:2 title "1" w l;
  replot "plot02.dat" using 1:2 title "2" w l;
  replot "plot03.dat" using 1:2 title "3" w l;
  replot "plot04.dat" using 1:2 title "4" w l;
  replot "plot05.dat" using 1:2 title "5" w l;
  replot "plot06.dat" using 1:2 title "6" w l;
  replot "plot07.dat" using 1:2 title "7" w l;
  pause -1
'
