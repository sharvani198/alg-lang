


def find_crossing_max_subarray(arr,low, mid, high):
	leftSum = float('-inf')
	sum = 0
	leftLow,rightLow = low,high
	for i in range(mid, low-1, -1):
		sum+=arr[i]
		if sum>leftSum:
			leftSum = sum
			leftLow = i
	rightSum = float('-inf')
	sum=0
	for j in range(mid+1, high):
		sum+=arr[j]
		if sum>rightSum:
			rightSum = sum
			rightLow = j
	return (leftLow, rightLow, leftSum + rightSum)

def find_max_subarray(arr, low, high):
	if high==low:
		return (low, high, arr[low-1])
	mid = (low+high)/2
	(leftlow, lefthigh, leftsum) = find_max_subarray(arr, low, mid)
	(rightlow, righthigh, rightsum) = find_max_subarray(arr, mid+1, high)
	(crosslow, crosshigh, crosssum) = find_crossing_max_subarray(arr, low, mid, high)
	if leftsum>rightsum and leftsum>crosssum:
		return (leftlow, lefthigh, leftsum)
	elif rightsum>leftsum and rightsum>crosssum:
		return (rightlow, righthigh, rightsum)
	elif crosssum>leftsum and crosssum> rightsum:
		return (crosslow, crosshigh, crosssum)


arr = [13,-3,-25,20,-3,-16,-23,18,20,-7,12,-5,-22,15,-4,7]
arr1= [-4,-50,7,-3]
(low,high, sum) = find_max_subarray(arr, 0, len(arr))

print (low, high, sum)