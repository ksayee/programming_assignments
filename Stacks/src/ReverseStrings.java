// Write a program to reverse a String using Stacks.

public class ReverseStrings {
	
	int top;
	int size;
	char[] stk;
	
	public ReverseStrings(int size)
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
		else if(top+1==size)
		{
			System.out.println("Stack is full");
		}
		else
		{
			top++;
			stk[top]=data;
		}
	}
	
	public char pop()
	{
		char ch='0';
		if(top==-1)
			System.out.println("Stack is empty");
		else
		{
			ch=stk[top];
			top--;
		}
			return ch;
	}
	
	public static String reverse(String str)
	{
		int len=str.length();
		String rev="";
		ReverseStrings sk = new ReverseStrings(len);
		
		for(int i=0; i<len;i++)
		{
			sk.push(str.charAt(i));
		}
		
		while(sk.top!=-1)
		{
			rev=rev+sk.pop();
		}
		return rev;
	}
	
	public static void main(String[] args)
	{
		String str="kartiksayee";
		System.out.println("The reverse of the String is: "+reverse(str));
	}
}
