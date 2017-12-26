def counting_sort(a, k):
	c = [0]*(k+1)
	b = [0]*(len(a)+1)
	for i in range(0, len(a)):
		c[a[i]] = c[a[i]]+1
	for i in range(1,k+1):
		c[i]=c[i]+c[i-1]
	for i in range(len(a)-1,-1,-1):
		b[c[a[i]]] = a[i]
		c[a[i]]-=1
	return b[1:]

# arr = [2, 5, 3, 0, 2, 3, 0, 3]
# brr = counting_sort(arr, 5)
# print brr