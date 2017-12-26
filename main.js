filename = 'ints';
choice = 6;
if(process.argv.length > 2) {
	filename = process.argv[2];
	choice = parseInt(process.argv[3]);
}
var fs = require('fs');
var arr = fs.readFileSync(filename).toString().trim().split("\n").map((i) => Number(i.trim()));

d1 = Date.now();
switch (choice) {
	case 1:
		choiceStr = "insertion sort"
		insertionSort = require('./insertion_sort.js');
		insertionSort(arr);
		break;
	case 2:
		choiceStr = "merge sort"
		mergeSort = require('./merge_sort.js');
		arr = mergeSort.mergeSort(arr, 0, arr.length -1);
		break;	
	case 3:	
		choiceStr = "heap sort"
		heapSort = require('./heap_sort.js')
		heapSort.heapSort(arr)
		break
	case 4:	
		choiceStr = "quick sort"
		quickSort = require('./quick_sort.js')
		quickSort.quickSort(arr, 0, arr.length -1)
		break	
	case 5:	
		choiceStr = "counting sort"
		countingSort = require('./counting_sort.js')
		arr=countingSort.countingSort(arr, arr.length)
		break	
	case 6:	
		choiceStr = "default sort (insertion for small size then quicksort)"
		arr = arr.sort((a,b)=> a-b) //since default is alphabetical sort, have to pass a comaprator func
		break	
	default:
		choiceStr = "No such sort"
		break;
}

d2 = Date.now();
if(isSorted(arr)) {
	console.log("Javascript = ", choiceStr, ", sorted " , meaningfulArrayLength(arr.length) ,  " numbers in ", (d2 - d1)/1000.00 , " seconds");
}
else 
	console.log("DID NOT SORT CORRECTLY");

function meaningfulArrayLength(length){
	THOUSAND = 1000
	MILLION = 1000000
	meaningfulArrayLength = ""
	if(length >= THOUSAND)
		if(length >=MILLION)
			meaningfulArrayLength = (length/MILLION) + " Million"
		else
			meaningfulArrayLength = (length/THOUSAND) + " Thousand"
	else
		meaningfulArrayLength = (length)
	return meaningfulArrayLength
}

function isSorted(arr) {
    var len = arr.length - 1;
    for(var i = 0; i < len; ++i) {
        if(arr[i] > arr[i+1]) {
            return false;
        }
    }
    return true;
}