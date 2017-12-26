
def parent(i):
	return i/2

def left(i):
	return 2*i+1 # since arrays are zero indexed there is an extra +1

def right(i):
	return 2*i+2

def max_heapify(arr, n, i):
	# arr = a['arr']
	l = left(i)
	r = right(i)
	largest = i
	if l<n and arr[i] < arr[l]:
		largest=l
	if r<n and arr[largest] < arr[r]:
		largest = r
	if largest!=i:
		arr[i],arr[largest] = arr[largest], arr[i]
		max_heapify(arr, n, largest)

def build_max_heap(arr):
	# a['heapsize'] = len(a['arr']) - 1
	n = len(arr)
	for i in range(n, -1, -1):
		max_heapify(arr, n, i)

def heap_sort(arr):
	build_max_heap(arr)
	for i in range(len(arr)-1, 0, -1):
		arr[i], arr[0] = arr[0], arr[i]
		max_heapify(arr, i, 0)
