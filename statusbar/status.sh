#!/bin/bash
while true
        do
	#data
	cpu=$(python ~/.i3/statusbar/cpu_percent.py)
        user_procs=$(ps -ef|grep -c $USER)
	top_proc=$(bash ~/.i3/statusbar/top_proc.sh)
        coretemp=$(bash ~/.i3/statusbar/coretemp.sh)

	echo "[$(date) CPU:$cpu]"\
	     "[Procs:$user_procs  Top:$top_proc CT:$coretemp]"
done	
