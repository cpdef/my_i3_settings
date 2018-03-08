#!/bin/bash
a=$(top -b -n 1 -u $USER)
a=${a#*$USER}
a=${a%%$USER*}
a=$(echo $a)
a=${a% [0-9]*}
a=${a#* * * * * * }
#echo $a
echo ${a##* }:${a%% *} 
