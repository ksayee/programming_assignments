// Write a program to print all the number pair whose sum are the same.
import java.util.HashMap;

public class FourElementSum {
	
	public static void printPairSum(int[] arr)
	{
		HashMap<Integer,Pair> map=new HashMap<Integer,Pair>();
		int sum=0;
		
		for(int i=0;i<arr.length-1;i++)
		{
			for(int j=i+1;j<arr.length;j++)
			{
				sum=arr[i]+arr[j];
				if(map.containsKey(sum))
				{
					Pair p=map.get(sum);
					System.out.println("The four sum numbers are: "+arr[i]+" "+arr[j]+" "+arr[p.first]+" "+arr[p.second]);
				}
				else
				{
					map.put(sum,new Pair(i,j));
				}
			}
		}
	}
		
	public static void main(String[] args)
	{
		int[] arr={3,4,7,1,2,9,8};
		printPairSum(arr);
	}
}
