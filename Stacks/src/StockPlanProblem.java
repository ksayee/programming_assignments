// Write a program to list the next greater element for all the elements in an array.

public class StockPlanProblem {
	
	int top;
	int size;
	int[] stk;
	
	public StockPlanProblem(int size)
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
		int rtn=0;
		if(top==-1)
			System.out.println("Stack is Empty");
		else
		{
			rtn=stk[top];
		}
		return rtn;
	}
		
	public static void stockplan(int[] arr)
	{
		StockPlanProblem sk=new StockPlanProblem(arr.length);
		sk.push(0);
		int[] s=new int[arr.length];
		s[0]=1;
		for(int i=1;i<arr.length;i++)
		{
			while(!sk.isEmpty() && arr[sk.peek()]<arr[i])
			{
				sk.pop();
			}
			if(sk.isEmpty())
			{
				s[i]=i+1;
			}
			else
			{
				s[i]=i-sk.peek();
			}
			sk.push(i);
		}
		
		for(int j=0;j<s.length;j++)
		{
			System.out.print(s[j]+" ");
		}
		System.out.println();
	}
	
	public static void main(String[] args)
	{
		//int[] arr1={100,65,70,110,80,90,120};
		int[] arr1={10, 4, 5, 90, 120, 80};
		stockplan(arr1);
	}
}
