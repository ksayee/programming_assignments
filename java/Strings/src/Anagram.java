// Write a program check if two strings are Anagrams or NOT.

import java.util.HashMap;
import java.util.Arrays;

public class Anagram {
	
	public static boolean checkAnagram1(String str1,String str2)
	{
		HashMap<Character,Integer> map=new HashMap<Character,Integer>();
		
		if(str1.length()!=str1.length())
			return false;
		
		for(int i=0;i<str1.length();i++)
		{
			char key=str1.charAt(i);
			if(map.containsKey(key))
			{
				int val=map.get(key);
				map.put(key, val+1);
			}
			else
			{
				map.put(key,1);
			}
		}
		
		
		for(int j=0;j<str2.length();j++)
		{
			char key=str2.charAt(j);
			if(map.containsKey(key) && map.get(key)>0)
			{
				int val=map.get(key);
				map.put(key, val-1);
			}
			else
				return false;
		}
		return true;
	}
	
	public static boolean checkAnagram2(String str1,String str2)
	{
		if(str1.length()!=str2.length())
			return false;
		char[] c_arr1=str1.toCharArray();
		char[] c_arr2=str2.toCharArray();
		
		Arrays.sort(c_arr1);
		Arrays.sort(c_arr2);
		
		String t_str1=new String(c_arr1);
		String t_str2=new String(c_arr2);
		
		if(t_str1.equals(t_str2))
			return true;
		else
			return false;
	}
	
	public static void main(String[] args)
	{
		String str1="LISTEN";
		String str2="SILENT";
		if(checkAnagram1(str1,str2))
			System.out.println("Strings are Anagrams");
		else
			System.out.println("Strings are NOT Anagrams");
		
		if(checkAnagram2(str1,str2))
			System.out.println("Strings are Anagrams");
		else
			System.out.println("Strings are NOT Anagrams");
	}
}
