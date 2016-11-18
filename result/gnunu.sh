
gnuplot -e '
  plot "example01.dat" using 1:2 w l;
  replot "example02.dat" using 1:2 w l;
  replot "example03.dat" using 1:2 w l;
  replot "example04.dat" using 1:2 w l;
  replot "example05.dat" using 1:2 w l;
  replot "example06.dat" using 1:2 w l;
  replot "example07.dat" using 1:2 w l;
  pause -1
'
