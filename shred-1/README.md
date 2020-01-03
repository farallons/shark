# Karatsuba Algorithm 
## python

----

Set up virtualenv folder using Python3 and activate 
```
virtualenv -p python3 venv
```

Run 
```
pip3 install -r requirements.txt
chmod u+x karatsuba-timing.sh
```

Run the base-10 Karabatsu algorithm to multiply two non-negative integers _x_ and _y_
``` 
python3 karabatsu10.py <x> <y>
```

Run the base-2 Karabatsu algorithm to multiply two non-negative integers _x_ and _y_
``` 
python3 karabatsu2.py <x> <y>
```

Check the timing on the multiplication of two 8192 digit numbers with both algorithms and without either algorithm 
```
./karatsuba-timing.sh
```

###### Tested on Ubuntu 19.10