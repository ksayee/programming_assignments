// Write a program print count of the number of words in a given string.
import java.util.HashMap;

public class WordCount {
	
	public static int getWordCount(String str)
	{
		int count=0;
		
		for(int i=0;i<str.length();i++)
		{
			if(Character.isWhitespace(str.charAt(i)) || i+1==str.length())
			{
				count++;
			}
		}
		return count;
	}
	
	public static void main(String[] args)
	{
		String str= "This is my first count program";
		System.out.println("Count of Words: " + getWordCount(str));
	}

}
