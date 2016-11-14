// Write a program to get the length of valid parenthesis.

public class ValidParenthesisLength {
	
	int top;
	int size;
	char[] stk;
	
	public ValidParenthesisLength(int size)
	{
		top=-1;
		this.size=size;
		stk=new char[size];
	}
	
	public void push(char data)
	{
		if(top==-1)
		{
			top++;
			stk[top]=data;
		}
		else
		{
			top++;
			stk[top]=data;
		}
	}
	
	public void pop()
	{
		top--;
	}
	
	public char peek()
	{
		return stk[top];
	}
	
	public boolean isEmpty()
	{
		if(top==-1)
			return true;
		else
			return false;
	}
	
	public static void main(String[] args)
	{
		//String str="((()";
		//String str=")()())";
		String str="()(()))))";
		ValidParenthesisLength stk=new ValidParenthesisLength(str.length());
		char ch;
		int cnt=0;
		for(int i=0;i<str.length();i++)
		{
			ch=str.charAt(i);
			if(ch=='(')
			{
				stk.push(ch);
			}
			else
			{
				if(!stk.isEmpty())
				{
					stk.pop();
					cnt=cnt+2;
				}
			}
		}
		System.out.println("Length of Valid parenthesis is: "+cnt);
	}
}
