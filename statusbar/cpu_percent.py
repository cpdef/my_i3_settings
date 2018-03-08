#!/usr/bin/python3
import time
		
def _cpu_percentage(cpu_name, waittime):
	prev_stat = [i .split(" ") for i in open("/proc/stat")]
	time.sleep(waittime)
	curr_stat = [i .split(" ") for i in open("/proc/stat")]
	cpus = []
	for i in curr_stat:
		if i[0][:3] == "cpu":
			cpus.append(i[0])
			
			
	for j, w in enumerate(cpus):
		if w == cpu_name:
			i = j
	prev = prev_stat[i]
	curr = curr_stat[i]
	PrevIdle = int(prev[5])+int(prev[6])
	Idle = int(curr[5])+int(curr[6])
	
	PrevNonIdle = int(prev[2])+int(prev[3])+int(prev[4])+int(prev[7])+int(prev[8])+int(prev[9])
	NonIdle = int(curr[2])+int(curr[3])+int(curr[4])+int(curr[7])+int(curr[8])+int(curr[9])
	
	PrevTotal = PrevIdle + PrevNonIdle
	Total = Idle + NonIdle
	
	totald = Total - PrevTotal
	idled = Idle - PrevIdle
	return (totald - idled)/totald*100
	
def get_percentage():
    testnr = 3
    testresult = 0
    for i in range(3):
        testresult += _cpu_percentage("cpu", 1)
    
    return round(testresult/testnr, 2)

if __name__ == '__main__':
	print(get_percentage())
