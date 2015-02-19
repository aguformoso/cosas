#!/bin/bash

for f in $(ls *.txt)
do
	encoding=$(file -I $f | cut -d = -f 2)
	iconv -f $encoding -t utf-8 $f > $f"2"
done
