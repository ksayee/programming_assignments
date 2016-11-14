// Write a program to return fixed point in the arrary such that arr[i]=i.

public class ReturnIndxElement {
	
	public static int getFixedPoint(int[] arr)
	{
		int left=0;
		int right=arr.length-1;
		int mid=(left+right)/2;
		
		while(left<right)
		{
			if(arr[mid]==mid)
				return mid;
			else
			{
				if(mid>arr[mid])
					left=mid+1;
				else
					right=mid-1;
			}
			mid=(left+right)/2;
		}
		return -1;
	}
		
	public static void main(String[] args)
	{
		//int[] arr={10, -5, 0, 3, 7};
		int[] arr={0, 2, 5, 8, 17};
		//int[] arr={-10, -5, 3, 4, 7, 9};
		System.out.println("The fixed point in this arrary is: "+getFixedPoint(arr));
	}
}