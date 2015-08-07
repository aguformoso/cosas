#!/bin/bash

# Script that converts files to UTF-8 encoding
# The script creates the "conv" directory and dumps the converted files in there
# Agustín Formoso
# LACNIC - Aug 2015

which file > /dev/null 2>&1  || exit 1
which iconv > /dev/null 2>&1 || exit 1

dir=conv
mkdir $dir

for f
do
	encoding=$(file -I $f | cut -d = -f 2)
	iconv -f $encoding -t utf-8 $f > $dir/$f
done
