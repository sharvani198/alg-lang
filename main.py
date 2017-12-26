import time;
from sys import argv;
from insertion_sort import insertion_sort;
from merge_sort import merge_sort;
from heap import heap_sort;
from quick_sort import quick_sort;
from counting_sort import counting_sort;

def readFromFile(fileName):
	with open(fileName) as file:
		lines = [int(line.strip()) for line in file]
	return lines;
def meaningfulArrayLength(length):
	THOUSAND = 1000
	MILLION = 1000000
	meaningfulArrayLength = ""
	if length >= THOUSAND:
		if length >=MILLION:
			meaningfulArrayLength = str(length/MILLION) + " Million"
		else:
			meaningfulArrayLength = str(length/THOUSAND) + " Thousand"
	else:
		meaningfulArrayLength = str(length)
	return meaningfulArrayLength

if __name__== "__main__":
	fileName  = 'ints';
	choice = 6;
	if(len(argv) > 1):
		fileName = argv[1];
		choice  = int(argv[2]);

	integers = readFromFile(fileName);

	before = time.time();

	choiceStr = ""

	if choice == 1:
		choiceStr = "insertion sort"
		insertion_sort(integers);
	elif choice == 2:
		choiceStr = "merge sort"
		p=0;
		r= len(integers);
		merge_sort(integers, p, r-1);
	elif choice == 3:
		choiceStr = "heap sort"
		heap_sort(integers)
	elif choice == 4:
		choiceStr = "quick sort"
		quick_sort(integers, 0, len(integers)-1)
	elif choice == 5:
		choiceStr = "counting sort"
		integers = counting_sort(integers, len(integers))
	elif choice == 6:
		choiceStr = "default sort(timsort - a hybrid of merge and insertion)"
		integers = sorted(integers)
	else:
		choiceStr ="no such sort"

	after = time.time();
	timediff = round(float(after - before),2);
	if sorted(integers) == integers:
		print "Python = ", choiceStr, ", sorted " ,meaningfulArrayLength(len(integers)) , " numbers in ", timediff , " seconds" ;
	else :
		print "DID NOT SORT CORRECTLY"