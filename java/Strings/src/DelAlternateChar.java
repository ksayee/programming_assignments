// Write a program to delete alternate repeated character.
import java.util.HashMap;
import java.util.Map;

public class DelAlternateChar {
	
	public static String processString(String str)
	{
		HashMap<Character,Integer> map=new HashMap<Character,Integer>();
		
		String tmp_str="";
		int cnt=1;
		
		for(int i=0;i<str.length();i++)
		{
			char ch=str.charAt(i);
			if(map.containsKey(ch))
			{
				if(cnt%2!=0)
				{
					tmp_str=tmp_str+str.charAt(i);
				}
				cnt++;
			}
			else
			{
				map.put(ch, 1);
				tmp_str=tmp_str+str.charAt(i);
			}
			
		}
		return tmp_str;
	}
		
	public static void main(String[] args)
	{
		String str="you got beautiful eyes";
		System.out.println("Original String:  "+str);
		System.out.println("New String:  "+processString(str));
	}
}
