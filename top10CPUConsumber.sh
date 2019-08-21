#!/bin/bash

echo "Time: `date`"
echo "Head 10 CPU Utilization process: "
echo "`ps -eo pcpu,pid,user,args | sort -k 1 -r | head -10`"
echo "######################################################"
echo ""


# set up cron job to monitor the server cpu consumers
