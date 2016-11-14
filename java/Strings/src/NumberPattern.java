// Write a program print the following pattern. 16 11 6 1 -4 1 6 11 16

public class NumberPattern {
	
	public static void printPattern(int n,int m,boolean flg)
	{
		System.out.print(m+" ");
		
		if(!flg && n==m)
			return;
		
		if(flg)
		{
			if(m-5>0)
			{
				printPattern(n,m-5,true);
			}
			else
			{
				printPattern(n,m-5,false);
			}
		}
		else
		{
			printPattern(n,m+5,false);
		}
	}
	
	public static void main(String[] args)
	{
		int n=16;
		printPattern(n,n,true);
	}
}
