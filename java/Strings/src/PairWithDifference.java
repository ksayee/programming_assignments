// Write a program to print all the number pair whose sum are the same.

public class PairWithDifference {
	
	public static void printPairDiff(int[] arr,int diff)
	{
		for(int i=0;i<arr.length-1;i++)
		{
			for(int j=i+1;j<arr.length;j++)
			{
				if(Math.abs(arr[i]-arr[j])==diff)
					System.out.println("The difference pair numbers are: "+arr[i]+" "+arr[j]);
			}
		}
	}
		
	public static void main(String[] args)
	{
		int[] arr={5, 20, 3, 2, 50, 80};
		int diff=78;
		printPairDiff(arr,diff);
	}
}
