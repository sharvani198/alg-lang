def merge(arr, p, q, r):
	len1 = q-p+1
	len2=r-q
	lefthalf = [0]*len1
	righthalf = [0]*len2
	for i in range(0, len1):
		lefthalf[i] = arr[p+i]
	for j in range(0, len2):
		righthalf[j] = arr[q+1+j]
	i=0
	j=0
	k=p
	while i < len1 and j < len2:
	    if lefthalf[i] <= righthalf[j]:
	        arr[k]=lefthalf[i]
	        i=i+1
	    else:
	        arr[k]=righthalf[j]
	        j=j+1
	    k=k+1

	while i < len1:
	    arr[k]=lefthalf[i]
	    i=i+1
	    k=k+1

	while j < len2:
	    arr[k]=righthalf[j]
	    j=j+1
	    k=k+1


def merge_sort(arr, p, r):
	if p<r :
		q = (p+r)/2
		merge_sort(arr, p, q)
		merge_sort(arr, q+1, r)
		merge(arr, p, q, r)
