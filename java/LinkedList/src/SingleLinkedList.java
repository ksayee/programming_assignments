
public class SingleLinkedList {

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
	public static void main(String[] args)
	{
		SingleLinkedList lnk= new SingleLinkedList();
		lnk.add(10);
		lnk.add(20);
		lnk.add(30);
		lnk.add(40);
		lnk.add(50);
		lnk.display();
		lnk.reverse();
		lnk.display();
	}
}
