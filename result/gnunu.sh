
gnuplot -e '
  plot "example01.dat" using 1:2;
  replot "example02.dat" using 1:2;
  replot "example03.dat" using 1:2;
  replot "example04.dat" using 1:2;
  replot "example05.dat" using 1:2;
  replot "example06.dat" using 1:2;
  replot "example07.dat" using 1:2;
  pause -1
'
