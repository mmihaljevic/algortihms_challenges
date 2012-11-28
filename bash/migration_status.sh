#!/bin/bash
while read a b
do
nc -v -z -w 1 $a $b
done<hosts.txt
