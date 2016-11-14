// Write a program to reverse the words and letters in a string.

public class ReverseWordsandLetters {
	
	public static String printReverseWords(String str)
	{
		if(str.length()==1)
		{
			return str;
		}
		else
		{
			String rev;
			rev=str.charAt(str.length()-1)+printReverseWords(str.substring(0,str.length()-1));
			return rev;
		}
	}
	
	public static void main(String[] args)
	{
		String str= "the sky is blue";
		System.out.println(printReverseWords(str));
	}
}
