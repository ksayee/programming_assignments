// Write a program to implement a stack.

public class ReverseStacks {
	
	int top;
	int size;
	int[] stk;
	
	public ReverseStacks(int size)
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
	
	public boolean isEmpty()
	{
		if(top==-1)
			return true;
		else 
			return false;
	}
	
	public int peek()
	{
		return stk[top];
	}
	
	public void reverse()
	{
		if(!isEmpty())
		{
			int temp=peek();
			pop();
			reverse();
			insertElement(temp);
		}
	}
	
	public void insertElement(int data)
	{
		if(isEmpty())
		{
			push(data);
		}
		else
		{
			int temp=peek();
			pop();
			insertElement(data);
			push(temp);
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
		ReverseStacks stk=new ReverseStacks(5);
		System.out.println("Adding Elemnts");
		stk.push(10);
		stk.push(20);
		stk.push(30);
		stk.push(40);
		stk.push(50);
		System.out.println("Display Elements");
		stk.display();
		System.out.println("Reversing Stack");
		stk.reverse();
		System.out.println("Display Elemnts");
		stk.display();
	}
}
