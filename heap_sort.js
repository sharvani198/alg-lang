

parent = (i) => parseInt(i/2)
left = (i) => 2*i+1 
right = (i) => 2*i+2

max_heapify = function(arr, n, i) {
	l= left(i)
	r= right(i)
	largest= i
	if(l<n && arr[l]>arr[i])
		largest = l
	if(r<n && arr[r]>arr[largest])
		largest = r
	if(largest!=i)
	{
		tmp = arr[i]
		arr[i]=arr[largest]
		arr[largest]= tmp
		max_heapify(arr, n, largest)
	}
}

build_max_heap = function(arr) {
	n=arr.length
	for(i=n;i>=0;i--)
		max_heapify(arr, n, i)
}

exports.heapSort = function(arr) {
	build_max_heap(arr)
	for(i=arr.length -1; i>0;i--){
		tmp = arr[0]
		arr[0] = arr[i]
		arr[i]=tmp
		max_heapify(arr, i, 0)
	}
	return arr
}
