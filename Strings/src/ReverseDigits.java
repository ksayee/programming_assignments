// Write a program to reverse the numbers.

public class ReverseDigits {
	
	public static int printReverseDigits(int digit)
	{
		if(digit/10==0)
		{
			return digit;
		}
		else
		{
			int rev;
			rev=(digit/10)*10+printReverseDigits(digit%10);
			return rev;
		}
	}
	
	public static void main(String[] args)
	{
		int digit=678;
		System.out.println(printReverseDigits(digit));
	}
}
