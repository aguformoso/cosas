#!/bin/bash
#
#
#
noDeployFile() {
	echo "No hay archivo que especifique los deploys para la aplicación $1"
 }

DEPLOYFILENAME='deploys'
BASEDIR=$1
for app in $(ls -d $BASEDIR/* 2>/dev/null)
do
	# es necesario que la aplicación cuente con el archivo que indica los archivos que forman parte del deploy.

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
