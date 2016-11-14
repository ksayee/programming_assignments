// Write a program to implement a stack.

public class Stacks {
	
	int top;
	int size;
	int[] stk;
	
	public Stacks(int size)
	{
		top=-1;
		this.size=size;
		stk=new int[size];
	}
	
	public void push(int data)
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
	
	public void pop()
	{
		if(top==-1)
			System.out.println("Stack is empty");
		else
			top--;
	}
	
	public int peek()
	{
		return stk[top];
	}
	
	public void reverse()
	{
		if(top==-1)
			return;
		else
		{
			int tmp=peek();
			System.out.println("data :" + tmp);
			pop();
			reverse();
			push(tmp);
		}
	}
	
	public void display()
	{
		if(top==-1)
			System.out.println("Stack is empty");
		else
		{
			for(int i=0;i<=top;i++)
			{
				System.out.println(stk[i]);
			}
		}
	}
	
	public static void main(String[] args)
	{
		Stacks stk=new Stacks(5);
		System.out.println("Adding Elemnts");
		stk.push(10);
		stk.push(20);
		stk.push(30);
		stk.push(40);
		stk.push(50);
		System.out.println("Display Elements");
		stk.display();
	}
}
