#!/bin/sh

SIZE=1000
if [ "$1" != "" ]; then
    SIZE=$1
fi
START=$(date +%s)
python generator.py $SIZE ints
END=$(date +%s);
echo "$((END-START)) sec taken to generate $SIZE numbers"

echo "ALgorithms list
    1: INSERTION SORT
    2: MERGE SORT
    3: HEAP SORT
    4: QUICK SORT
    5: ALL
	"
read -p "Enter your choice: " input

execute_choice()
{
	CHOICE=$1

	START=$(date +%s);
	python main.py ints $CHOICE
	END=$(date +%s);
	echo "$((END-START)) sec taken by python."

	START=$(date +%s);
	node main.js ints $CHOICE
	END=$(date +%s);
	echo "$((END-START)) sec taken by js."

	START=$(date +%s);
	javac Sorts.java
	javac main.java
	java main ints $CHOICE
	END=$(date +%s);
	echo "$((END-START)) sec taken by java."
}

if [ "$input" -eq "5" ]; then
	echo "Executing all sorts. NB: This will take long for large input size, esp INSERTION SORT."
	for i in 1 2 3 4
	do
		execute_choice $i
	done
else
	execute_choice $input
fi
