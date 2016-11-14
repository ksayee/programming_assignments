// Write a program to reverse the numbers.

public class NumberSum {
	
	public static int SumNumbers(int digit)
	{
		int sum=0;
		while(digit!=0)
		{
			sum=sum+digit%10;
			digit=digit/10;
			if(digit==0 && sum>10)
			{
				digit=sum;
				sum=0;
			}
		}
		return sum;
	}
	
	public static void main(String[] args)
	{
		int digit=67898;
		System.out.println(SumNumbers(digit));
	}
}
