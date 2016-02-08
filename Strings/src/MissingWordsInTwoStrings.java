// Write a program print missing word from the second string which are present in the first String.
import java.util.HashMap;

public class MissingWordsInTwoStrings {
	
	public static void printMissingWords(String str1,String str2)
	{
		HashMap<String,Integer> map_str1=new HashMap<String,Integer>();
		
		int st=0,end=0;
		boolean flg=true;
		
		for(int i=0;i<str1.length();i++)
		{
			if(Character.isWhitespace(str1.charAt(i)) || i+1==str1.length())
			{
				if(i+1==str1.length())
				{
					end=i+1;
				}
				else
				{
					end=i;
				}
				flg=true;
				String key=str1.substring(st,end);
				if(map_str1.containsKey(key))
				{
					int val=map_str1.get(key);
					map_str1.put(key, val+1);
				}
				else
				{
					map_str1.put(key, 1);
				}
			}
			else
			{
				if(flg)
				{
					st=i;
					flg=false;
				}
			}
		}
		st=0;
		end=0;
		flg=true;
		for(int i=0;i<str2.length();i++)
		{
			if(Character.isWhitespace(str2.charAt(i)) || i+1==str2.length())
			{
				if(i+1==str2.length())
				{
					end=i+1;
				}
				else
				{
					end=i;
				}
				flg=true;
				String key=str2.substring(st,end);
				if(!map_str1.containsKey(key))
				{
					System.out.println(key);
				}
			}
			else
			{
				if(flg)
				{
					st=i;
					flg=false;
				}
			}
		}
	}
	
	public static void main(String[] args)
	{
		String str1= "Life is beautiful and not fair in real world";
		String str2= "beautiful and white world is san francisco";
		printMissingWords(str1,str2);
	}
}
