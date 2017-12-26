
merge = function(left, right) {
	var result = [],
		len1 = left.length;
		len2 = right.length;
	i = 0
	j = 0
	while (i< len1 && j< len2) {
		if(left[i]<=right[j]) {
			result.push(left[i++])
		} else {
			result.push(right[j++])
		}
	}
	return result.concat(left.slice(i)).concat(right.slice(j));
}

mergeSort = function(arr) {
	if(arr.length == 1) {
		return arr
	}
	const q = Math.floor(arr.length/2);
	const left = arr.slice(0,q)
	const right = arr.slice(q)
	return merge(this.mergeSort(left), this.mergeSort(right));
}


module.exports.merge = merge;
module.exports.mergeSort = mergeSort;