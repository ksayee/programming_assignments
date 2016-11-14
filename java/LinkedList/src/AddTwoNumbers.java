
public class AddTwoNumbers {

	Node head;
	Node tail;
	
	public void add(int data)
	{
		Node n=new Node(data);
		
		if(head==null)
		{
			head=n;
			tail=n;
		}
		else
		{
			Node temp=head;
			while(temp.next!=null)
			{
				temp=temp.next;
			}
			temp.next=n;
			tail=n;
		}
	}
	
	public void delete(int data)
	{
		Node temp=find(data);
		if(temp==null)
		{
			System.out.println("Node not found");
		}
		else
		{
			if(head==temp)
			{
				head=head.next;
			}
			else
			{
				Node prev=head;
				Node curr=head.next;
				while(curr!=temp)
				{
					curr=curr.next;
					prev=prev.next;
				}
				if(curr.next==null)
				{
					prev.next=null;
					tail=prev;
				}
				else
				{
					prev.next=curr.next;
				}
			}
			System.out.println("Node Deleted");
		}
	}
	
	public Node find(int data)
	{
		Node temp=head;
		while(temp!=null)
		{
			if(temp.data==data)
				return temp;
			else
			{
				temp=temp.next;
			}
		}
		return null;
	}
	
	public void display()
	{
		Node temp=head;
		while(temp!=null)
		{
			System.out.println(temp.data);
			temp=temp.next;
		}
	}
	
	public void reverse()
	{
		Node temp=head;
		System.out.println("Reversing list");
		reverselist(temp);
	}
	
	public void reverselist(Node temp)
	{
		if(temp.next==null)
		{
			head=temp;
			return;
		}
		else
		{
			reverselist(temp.next);
			temp.next.next=temp;
			temp.next=null;
			tail=temp;
		}
	}
	
	public int sum()
	{
		Node tmp=this.head;
		return find_sum(tmp,1);
	}
	
	
	public int find_sum(Node temp,int cnt)
	{
		if(temp.next==null)
		{
			int f=1;
			while(cnt--!=1)
			{
				f=f*10;
			}
			return temp.data*f;
		}
		else
		{
			int t=find_sum(temp.next,cnt+1);
			int f=1;
			while(cnt--!=1)
			{
				f=f*10;
			}
			return t+(temp.data*f);
		}
	}
	
	public static void create_newlist(int sum)
	{
		AddTwoNumbers lnk3=new AddTwoNumbers();
		while(sum/10!=0)
		{
			lnk3.add(sum%10);
			sum=sum/10;
		}
		lnk3.add(sum);
		lnk3.reverse();
		lnk3.display();
	}
	
	public static void main(String[] args)
	{
		AddTwoNumbers lnk1= new AddTwoNumbers();
		lnk1.add(7);
		lnk1.add(5);
		lnk1.add(9);
		lnk1.add(4);
		lnk1.add(6);
		System.out.println("First List");
		lnk1.display();
		AddTwoNumbers lnk2= new AddTwoNumbers();
		lnk2.add(8);
		lnk2.add(4);
		System.out.println("Second List");
		lnk2.display();
		int sum1=lnk1.sum();
		System.out.println("First Sum "+sum1);
		int sum2=lnk2.sum();
		System.out.println("Second Sum "+sum2);
		int final_sum=sum1+sum2;
		System.out.println("Final Sum "+final_sum);
		create_newlist(final_sum);
	}
}
