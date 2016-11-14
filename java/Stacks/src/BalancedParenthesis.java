// Write a program to check if parenthesis is Balanced or not.

public class BalancedParenthesis {
	
	int top;
	int size;
	char[] stk;
	
	public BalancedParenthesis(int size)
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
	
	public static void main(String[] args)
	{
		String str="([{}])[]{{([])}}";
		BalancedParenthesis stk=new BalancedParenthesis(str.length());
		char ch;
		boolean flg=true;
		for(int i=0;i<str.length();i++)
		{
			ch=str.charAt(i);
			if(ch=='{' || ch=='(' || ch=='[')
			{
				stk.push(ch);
			}
			else if((ch=='}' && stk.peek()=='{') || (ch==')' && stk.peek()=='(') || (ch==']' && stk.peek()=='['))
				stk.pop();
			else
			{
				flg=false;
				break;
			}
		}
		if(flg)
			System.out.println("Parenthesis is Balanced");
		else
			System.out.println("Parenthesis is NOT Balanced");
	}
}
