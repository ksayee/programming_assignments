// Write a program print each letter and the count of each letters in a string.
import java.util.HashMap;

public class LetterCountString {
	
	public static void getLeterCount(String str)
	{
		HashMap<Character,Integer> map=new HashMap<Character,Integer>();
		
		for(int i=0;i<str.length();i++)
		{
			if(!Character.isWhitespace(str.charAt(i)))
			{
				char key=str.charAt(i);
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
		}
		for(Character key: map.keySet())
		{
			System.out.println(key + ": " + map.get(key));
		}
	}
	
	public static void main(String[] args)
	{
		String str= "desert rose is the best of the best song ever song is rose";
		getLeterCount(str);
	}
}
