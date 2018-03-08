#!/bin/bash 
a=$(sensors)
c1=${a#*Core 1:}
from_c0=${a#*Core 0:}
c0=${from_c0%Core 1:*}
tc1=${c1%  (*}; tc1=${tc1##* }
tc0=${c0%  (*}; tc0=${tc0##* }
echo "$tc0 $tc1"

