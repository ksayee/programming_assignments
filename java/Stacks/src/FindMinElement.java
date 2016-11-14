// Write a program to implement a stack and find the minimum element in O(1).

public class FindMinElement {
	
	int top;
	int min_top;
	int size;
	int[] stk;
	int[] min;
	
	public FindMinElement(int size)
	{
		top=-1;
		min_top=-1;
		this.size=size;
		stk=new int[size];
		min=new int[size];
	}
	
	public void push(int data)
	{
		if(top==-1)
		{
			top++;
			min_top++;
			stk[top]=data;
			min[min_top]=data;
		}
		else if(top+1==size)
		{
			System.out.println("Stack is full");
		}
		else
		{
			top++;
			stk[top]=data;
			if(data<min[min_top])
			{
				min_top++;
				min[min_top]=data;
			}
		}
		printmin();
	}
	
	public void pop()
	{
		if(top==-1)
			System.out.println("Stack is empty");
		else
		{
			if(stk[top]==min[min_top])
			{
				top--;
				min_top--;
			}
			else
				top--;
			printmin();
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
	
	public void printmin()
	{
		if(top!=-1)
			System.out.println("Mininum Element: "+min[min_top]);
	}
	
	public static void main(String[] args)
	{
		FindMinElement stk=new FindMinElement(5);
		System.out.println("Adding Elemnts");
		stk.push(10);
		stk.push(11);
		stk.push(9);
		stk.push(15);
		stk.push(1);
		System.out.println("Display Elements");
		stk.display();
		System.out.println("Popping Elemnts");
		stk.pop();
		stk.pop();
		stk.pop();
		System.out.println("Display Elemnts");
		stk.display();
	}
}
