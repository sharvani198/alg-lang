exports.countingSort = function(a, k) {
	c = [...new Array(k+1)].map(()=> 0)
	len = a.length
	b = [...new Array(len+1)].map(()=> 0)
	for(i=0;i<len;i++)
		c[a[i]] = c[a[i]]+1
	for(i=1;i<=k;i++)
		c[i] = c[i]+c[i-1]
	for(i=len;i>=0;i--){
		b[c[a[i]]] = a[i]
		c[a[i]]--;
	}
	return b.slice(1)
}

// arr = [2, 5, 3, 0, 2, 3, 0, 3]
// brr = exports.countingSort(arr, 5)
// console.log(brr)