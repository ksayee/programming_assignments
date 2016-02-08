// Write a program print each word and the count of each words in a string.
import java.util.HashMap;

public class SymmetricNumbers {
	
	public static void getSymmetricNumbers(int[][] arr)
	{
		HashMap<Integer,Integer> map=new HashMap<Integer,Integer>();
		
		for(int i=0;i<arr.length;i++)
		{
			int first=arr[i][0];
			int second=arr[i][1];
			
			Integer val=map.get(second);
			
			if(val != null && val==first)
			{
				System.out.println("The Symmetric numbers are:" + first +" "+second);
			}
			else
			{
				map.put(first, second);
			}
		}
		
	}
	
	public static void main(String[] args)
	{
		int arr[][]=new int[5][2];
		arr[0][0]=11; arr[0][1]=20;
		arr[1][0]=30; arr[1][1]=40;
		arr[2][0]=5; arr[2][1]=10;
		arr[3][0]=40; arr[3][1]=30;
		arr[4][0]=10; arr[4][1]=5;
		getSymmetricNumbers(arr);
	}
}
