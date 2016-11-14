// Write a program print two numbers from an array which add to to a final given number.
import java.util.HashMap;

public class TwoNumberSum {
	
	public static void getTwoNumbers(int[] arr, int num)
	{
		HashMap<Integer,Integer> map=new HashMap<Integer,Integer>();
		
		int temp=0;
		for(int i=0;i<arr.length;i++)
		{
			temp=num-arr[i];
			if(map.containsKey(temp))
			{
				System.out.println("The two numbers are: " + temp + " "+ arr[i]);
			}
			else
			{
				map.put(arr[i], 1);
			}
		}
	}
	
	public static void main(String[] args)
	{
		int[] arr={1,4,45,6,10,8};
		int num=12;
		getTwoNumbers(arr,num);
	}
}
