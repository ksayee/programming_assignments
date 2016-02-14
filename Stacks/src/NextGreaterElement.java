// Write a program to list the next greater element for all the elements in an array.

public class NextGreaterElement {
	
	int top;
	int size;
	int[] stk;
	
	public NextGreaterElement(int size)
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
	
	public int pop()
	{
		int rtn=0;
		if(top==-1)
			System.out.println("Stack is empty");
		else
		{
			rtn=stk[top--];
		}
		return rtn;
	}
	
	public boolean isEmpty()
	{
		if(top==-1)
			return true;
		else 
			return false;
	}
	
	public static void NextGreElement(int[] arr)
	{
		NextGreaterElement sk=new NextGreaterElement(arr.length);
		sk.push(arr[0]);
		int element=0;
		int next=0;
		for(int i=1;i<arr.length;i++)
		{
			next=arr[i];
			if(!sk.isEmpty())
			{
				element=sk.pop();
				while(element<next)
				{
					System.out.println("Next Greater element of: "+element+" is  "+next);
					if(sk.isEmpty())
						break;
					else
						element=sk.pop();
				}
			}
			
			if(element>next)
				sk.push(element);
			sk.push(next);
		}
		
		while(!sk.isEmpty())
		{
			element=sk.pop();
			next=-1;
			System.out.println("Next Greater element of: "+element+" is  "+next);
		}
		
	}
	
	public static void main(String[] args)
	{
		int[] arr1={13, 7, 6, 12};
		System.out.println("New Input");
		NextGreElement(arr1);
		int[] arr2={4, 5, 2, 25};
		System.out.println("New Input");
		NextGreElement(arr2);
	}
}
