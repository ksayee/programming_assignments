
public class Queue {

	int front,rear,size;
	int[] que;
	
	public Queue(int size)
	{
		front=-1;
		rear=-1;
		this.size=size;
		que=new int[size];
	}
	
	public void enQueue(int data)
	{
		if(rear==size-1)
		{
			System.out.println("Queue is full");
		}
		else
		{
			if(front==-1)
			{
				front++;
				rear++;
				que[rear]=data;
			}
			else
			{
				rear++;
				que[rear]=data;
			}
		}
	}
	
	public void deQueue()
	{
		if(front==-1)
			System.out.println("Queue is empty");
		else
		{
			if(front==size-1)
			{
				front=-1;
				rear=-1;
			}
			else
			{
				front++;
			}
		}
	}
		
	public void display()
	{
		if(front==-1)
			System.out.println("Queue is empty");
		else
		{
			for(int i=front;i<=rear;i++)
			{
				System.out.println(que[i]);
			}
		}
	}
	
	public static void main(String[] args)
	{
		Queue que=new Queue(5);
		System.out.println("Adding Elemnts");
		que.enQueue(10);
		que.enQueue(20);
		que.enQueue(30);
		que.enQueue(40);
		que.enQueue(50);
		que.deQueue();
		que.deQueue();
		System.out.println("Display Elements");
		que.display();
	}
}
