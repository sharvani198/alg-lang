partition = function(arr, p,r) {
	x = arr[r]
	i=p-1
	for(j=p;j<r;j++) {
		if(arr[j]<=x) {
			i++;
			tmp = arr[i]
			arr[i]=arr[j]
			arr[j]=tmp
		}
	}
	tmp=arr[i+1]
	arr[i+1]=arr[r]
	arr[r]=tmp
	return i+1
}

exports.quickSort = function(arr, p, r) {
	if(p<r) {
		q = partition(arr, p, r)
		exports.quickSort(arr, p, q-1)
		exports.quickSort(arr, q+1, r)
	}
}


// arr = [33,8,78,56,3,20,4,18,10,2]
// exports.quickSort(arr, 0, arr.length-1)
// console.log(arr)