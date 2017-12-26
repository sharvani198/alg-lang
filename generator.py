from random import shuffle;
import time;
from sys import argv;

TEN_THOUSAND = 10000;


def writeIntegersToFile(integers, filename):
	file = open(filename, 'w');
	for i in integers:
		print>> file, i;
	return;

size  = TEN_THOUSAND;
filename = 'ints'
if(len(argv) > 1):
	size = int(argv[1])

integers = range(1,size+1);

shuffle(integers);
writeIntegersToFile(integers, filename);
