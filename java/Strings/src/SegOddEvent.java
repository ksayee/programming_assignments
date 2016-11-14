// Write a program to segregate odd and even numbers towards each end of the array.

public class SegOddEvent {
	
	public static void segregateOddEven(int[] arr)
	{
		int left=0;
		int right=arr.length-1;
		
		while(left<right)
		{
			while(left<right && arr[left]%2==0)
				left++;
			
			while(left<right && arr[right]%2==1)
				right--;
			if(left<right)
			{
				int tmp=arr[left];
				arr[left]=arr[right];
				arr[right]=tmp;
				left++;
				right--;
			}
		}
		System.out.println("New Array");
		for(int i=0;i<arr.length;i++)
		{
			System.out.print(arr[i]+" ");
		}
		System.out.println();
	}
		
	public static void main(String[] args)
	{
		int[] arr={12, 34, 45, 9, 8, 90, 3};
		System.out.println("Given Array");
		for(int i=0;i<arr.length;i++)
		{
			System.out.print(arr[i]+" ");
		}
		System.out.println();
		segregateOddEven(arr);
	}
}
