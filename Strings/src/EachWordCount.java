// Write a program print each word and the count of each words in a string.
import java.util.HashMap;

public class EachWordCount {
	
	public static void getWordCount(String str)
	{
		HashMap<String,Integer> map=new HashMap<String,Integer>();
		
		int st=0,end=0;
		boolean flg=true;
		
		for(int i=0;i<str.length();i++)
		{
			if(Character.isWhitespace(str.charAt(i)) || i+1==str.length())
			{
				if(i+1==str.length())
				{
					end=i+1;
				}
				else
				{
					end=i;
				}
				flg=true;
				String key=str.substring(st,end);
				if(map.containsKey(key))
				{
					int val=map.get(key);
					map.put(key, val+1);
				}
				else
				{
					map.put(key, 1);
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
		for(String key: map.keySet())
		{
			System.out.println(key + ": " + map.get(key));
		}
	}
	
	public static void main(String[] args)
	{
		String str= "desert rose is the best of the best song ever song is rose";
		getWordCount(str);
	}
}
