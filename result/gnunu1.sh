
gnuplot -e '
  plot "example0101.dat" using 1:2 w l;
  replot "example0102.dat" using 1:2 w l;
  replot "example0103.dat" using 1:2 w l;
  replot "example0104.dat" using 1:2 w l;
  replot "example0105.dat" using 1:2 w l;
  replot "example0106.dat" using 1:2 w l;
  replot "example0107.dat" using 1:2 w l;
  pause -1
'
