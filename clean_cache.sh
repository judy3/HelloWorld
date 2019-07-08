#!/bin/sh  

## This script is used to clean cache on linux when the memory usage is too high
## Usage method: ./$0

used=`free -m | awk 'NR==2' | awk '{print $3}'`  
free=`free -m | awk 'NR==2' | awk '{print $4}'`  

LOG_PATH="/var/log/mem.log"  #change the log path to wherever you need
echo "===========================" >> $LOG_PATH
date >> $LOG_PATH    
echo "Memory usage before | [Use：${used}MB][Free：${free}MB]" >> $LOG_PATH

#The memory usage threshold can be modified according to the real situation
if [ $free -le 1605 ] ; then  
                sync && echo 1 > /proc/sys/vm/drop_caches  
                sync && echo 2 > /proc/sys/vm/drop_caches  
                sync && echo 3 > /proc/sys/vm/drop_caches  
                used_ok=`free -m | awk 'NR==2' | awk '{print $3}'`  
                free_ok=`free -m | awk 'NR==2' | awk '{print $4}'`  
                echo "Memory usage after | [Use：${used_ok}MB][Free：${free_ok}MB]" >> $LOG_PATH 
                echo "OK" >> $LOG_PATH
else  
                echo "Not required" >> $LOG_PATH
fi  
exit 1  

# The crontab job can be defined to run it daily: 30 4 * * * /script_path/clean_cahe.sh
