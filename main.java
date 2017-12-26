import java.util.*;
import java.io.File;
import java.io.IOException;
class main
{
	private static String meaningfulArrayLength(int length){
		int THOUSAND = 1000;
		int MILLION = 1000000;
		String meaningfulArrayLength = "";
		if(length >= THOUSAND){
			if(length >=MILLION)
				meaningfulArrayLength = (length/MILLION) + " Million";
			else
				meaningfulArrayLength = (length/THOUSAND) + " Thousand";
		}
		else
			meaningfulArrayLength = length+"";
		return meaningfulArrayLength;
	}

	public static void main(String[] args) throws IOException{
		String fileName = "ints";
		int choice = 4;
		if(args.length > 0) {
			fileName = args[0];
			choice = Integer.parseInt(args[1]);
		}

		Scanner scanner = new Scanner(new File(fileName));
		List<Integer> ints = new ArrayList<Integer>();
		while(scanner.hasNextInt())
		{
		     ints.add(scanner.nextInt());
		}

		int[] arr = ints.stream().mapToInt(i -> i).toArray();

		// int[] arr = new Random().ints(size, 0, size).toArray();
		long t1 = System.currentTimeMillis();
		String choiceStr = "";
		switch(choice) {
			case 1:
				choiceStr = "insertion sort";
				Sorts.insertionSort(arr);
				break;
			case 2:
				choiceStr = "merge sort";
				arr = Sorts.mergeSort(arr, 0, arr.length -1);
				break;
			case 3:
				choiceStr = "heap sort";
				Sorts.heapSort(arr);
				break;
			case 4:
				choiceStr = "quick sort";
				Sorts.quickSort(arr, 0, arr.length - 1);
				break;
			default:
				choiceStr="no such sort";
				break;

		}
		long t2 = System.currentTimeMillis();
		if(Sorts.isSorted(arr)) {
			System.out.println("Java = "+ choiceStr+ ", sorted " + meaningfulArrayLength(arr.length) + " numbers in  " + (t2 - t1)/1000.00 + " seconds");
		}
		else 
			System.out.println("NOT SORTED");
	}
}