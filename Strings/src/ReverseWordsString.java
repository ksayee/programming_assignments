// Write a program to reverse the words in a string.

public class ReverseWordsString {
	
	public static void pritnReverseWords(String str)
	{
		int st=0,end=0;
		boolean flg=true;
		String temp="";
		
		for(int i=str.length()-1;i>=0;i--)
		{
			if(Character.isWhitespace(str.charAt(i)) || i==0)
			{
				if(i==0)
				{
					st=0;
				}
				else
				{
					st=i+1;
				}
				flg=true;
				temp=temp+" "+str.substring(st,end);
			}
			else
			{
				if(flg)
				{
					if(i+1==str.length())
					{
						end=i+1;
					}
					else
					{
						end=i+1;
					}
					flg=false;
				}
			}
		}
		System.out.println("The new String is: "+ temp);
	}
	
	public static void main(String[] args)
	{
		String str= "the sky is blue";
		pritnReverseWords(str);
	}
}
