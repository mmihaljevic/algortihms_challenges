#!/bin/bash
# call ./migration_status <hosts_file> <port_A> <port_B>

while read host
do

if nc -w 1 -z $host $2 &> /dev/null; then 
    echo $host $2 
fi

if nc -w 1 -z $host $3 &> /dev/null; then           
    echo $host $3 
fi
done<$1
