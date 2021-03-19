#!/bin/bash
for filename in ./data/*.txt; do
	splits=$(echo $filename | tr "_" "\n")
	echo ${splits[2]}
	# python3 plot.py "$filename"
done