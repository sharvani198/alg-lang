
public class Sorts
{
	public static int[] insertionSort(int[] arr)
	{
		for(int j=1;j<arr.length; j++) {
			int key = arr[j];
			int i = j - 1;
			while(i>=0 && arr[i]>key) {
				arr[i+1] = arr[i];
				i--;
			}
			arr[i+1] = key;
		}
		return arr;
	}

	private static void merge(int[] arr, int p, int q, int r)
	{
		int len1 = q-p+1;
		int len2 = r-q;
		int[] left = new int[len1];
		int[] right = new int[len2];
		for(int i=0;i<len1;i++)
			left[i] = arr[p+i];
		for(int j=0;j<len2;j++)
			right[j] = arr[q+j+1];
		int i = 0;
		int j = 0;
		int k = p;
		while(i<len1 && j<len2) {
			if(left[i]<=right[j]){
				arr[k] = left[i];
				i++;
			} else {
				arr[k] = right[j];
				j++;
			}
			k++;
		}

		while(i<len1) 
		{	
			arr[k] = left[i];
			k++;
			i++;
		}

		while(j<len2) 
		{	
			arr[k] = right[j];
			k++;
			j++;
		}
	}

	public static int[] mergeSort(int[] arr, int p, int r)
	{
		if(p<r){
			int q = (p+r)/2;
			mergeSort(arr, p, q);
			mergeSort(arr, q+1, r);
			merge(arr, p, q, r);
		}
		return arr;
	}

	public static boolean isSorted(int[] a) {
	    for (int i = 0; i < a.length - 1; i++) {
    	    if (a[i] > a[i + 1]) {
        	    return false; // It is proven that the array is not sorted.
        	}
    	}

    	return true; // If this part has been reached, the array must be sorted.
	}

	private static void heapify(int[] arr, int n, int i) {
		int left = 2*i+1;
		int right = 2*i+2;
		int largest=i;
		if(left<n && arr[left]>arr[i])
			largest=left;
		if(right<n && arr[right]>arr[largest])
			largest=right;
		if(largest!=i)
		{
			int tmp = arr[i];
			arr[i]=arr[largest];
			arr[largest]=tmp;
			heapify(arr, n, largest);
		}
	}

	public static void heapSort(int[] arr) {
		int n = arr.length;
		for(int i=n;i>=0;i--)
			heapify(arr, n, i);

		for(int i=n-1;i>0;i--) {
			int tmp=arr[0];
			arr[0]=arr[i];
			arr[i]=tmp;
			heapify(arr,i,0);
		}


	}

	private static int partition(int[] arr, int p, int r) {
		int x = arr[r]; //pivot element
		int i = p-1;//to keep track of a possible q
		for(int j =p; j<r;j++) {
			if(arr[j]<=x) {
				i++;
				int tmp = arr[i];
				arr[i]=arr[j];
				arr[j]=tmp;
			}
		}
		int tmp = arr[i+1];//put q in proper place such that 
		//elements before q are lesser and after are greater than q
		arr[i+1] = arr[r];
		arr[r] = tmp;
		return i+1;
	}

	public static void quickSort(int[] arr, int p, int r) {
		if(p<r) {
			int q = partition(arr, p, r);
			quickSort(arr, p, q-1);
			quickSort(arr, q+1, r);
		}
	}

    static void printArray(int arr[])
    {
        int n = arr.length;
        for (int i=0; i<n; ++i)
            System.out.print(arr[i] + " ");
        System.out.println();
    }

	// public static void main(String[] args) {
	// 	int[] arr = {22,43,3,7,88,67,35,99,76,82,90,156,211,4,71};
	// 	printArray(arr);
	// 	quickSort(arr, 0, arr.length -1);
	// 	printArray(arr);
	// }

}