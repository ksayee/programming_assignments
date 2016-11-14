// Write a program print the parenthesis pattern.

public class ParenthesisPattern {
	
	public static void printPattern(int n,int open, int close, String str)
	{
		if(close==n)
		{
			System.out.println(str);
			return;
		}
		else
		{
			if(open<n)
			{
				printPattern(n,open+1,close,str+'{');
			}
			if(open>close)
			{
				printPattern(n,open,close+1,str+'}');
			}
		}
	}
	
	public static void main(String[] args)
	{
		int n=2;
		printPattern(n,0,0,"");
	}
}
