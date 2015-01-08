#!/bin/bash
#
#
#
noDeployFile() {
	echo "No hay archivo que especifique los deploys para la aplicación $1"
 }

DEPLOYFILENAME='deploys'
BASEDIR='/Users/agustin/git/cosas'
for app in $(ls -d $BASEDIR/* 2>/dev/null)
do
	[ -f $app/$DEPLOYFILENAME ] || continue


	for deploy in $(ls -d $app/* 2>/dev/null) 
	do
		for file in $(cat $app/$DEPLOYFILENAME)
		do
			echo $deploy
			find $deploy -name $file
		done
	done
done

exit 0
