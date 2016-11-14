// Write a program to check if a string has unique characters.
// Easy way is to use a HashMap and if any character is existing in hashMap returns false else true.
// This method is using no data structure

public class UniqueCharacters {
	
	public static boolean checkUniquechar(String str)
	{
		int[] arr=new int[256];
		
		//char[] chr=str.toCharArray();
		
		for(int i=0;i<arr.length;i++)
		{
			arr[i]=0;
		}
		
		/*for(int j=0;j<chr.length;j++)
		{
			if(arr[chr[j]]>0)
				return false;
			else
				arr[chr[j]]++;
		}*/
		
		for(int j=0;j<str.length();j++)
		{
			if(arr[str.charAt(j)]>0)
				return false;
			else
				arr[str.charAt(j)]++;
		}
		return true;
	}
	
	public static void main(String[] args)
	{
		String str= "mary";
		System.out.println(checkUniquechar(str));
	}
}
