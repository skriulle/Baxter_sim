for i in `seq 1 8`
do
cd "ex0$i"
./gnunu.sh
mv plot_torque.png "../img/plot_tprque_0$i.png"
echo "$i done"
cd ..
done
