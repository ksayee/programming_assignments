// Write a program check if 2 strings are Anagrams or NOT.
import java.util.HashMap;
import java.util.Map;

public class Issomorphic_Strings {
	
	public static boolean checkIssomorphic(String str1,String str2)
	{
		HashMap<Character,Character> map=new HashMap<Character,Character>();
		
		if(str1.length()!=str1.length())
			return false;
		if(str1.length()==0 && str2.length()==0)
			return false;
		
		for(int i=0;i<str1.length();i++)
		{
			if(map.containsKey(str1.charAt(i)))
			{
				if (str2.charAt(i)!=map.get(str1.charAt(i)))
					return false;
			}
			else
			{
				for(Map.Entry<Character, Character> entry: map.entrySet())
				{
					if(entry.getValue().equals(str2.charAt(i)))
						return false;
				}
				map.put(str1.charAt(i),str2.charAt(i));
			}
		}
		return true;
	}
		
	public static void main(String[] args)
	{
		String str1="aab";
		String str2="ssy";
		if(checkIssomorphic(str1,str2))
			System.out.println("Strings are Issomorphic");
		else
			System.out.println("Strings are NOT Issomorphic");
	}
}
