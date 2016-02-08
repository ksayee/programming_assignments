// Write a program to compress a string and to extend a string.

public class StringCompressandExtend {
	
	public static String doCompress(String str)
	{
		String fnl_str="";
		int cnt=1;
		char prev=str.charAt(0);
		for(int i=1;i<str.length();i++)
		{
			if(str.charAt(i)==prev)
			{
				cnt++;
			}
			else
			{
				fnl_str=fnl_str+prev+cnt;
				prev=str.charAt(i);
				cnt=1;
			}
			
		}
		fnl_str=fnl_str+prev+cnt;
		return fnl_str;
	}
	
	public static String doExtend(String str)
	{
		String fnl_str="";
		char tmp=str.charAt(0);
		for(int i=0;i<str.length();i++)
		{
			if((str.charAt(i)>='a' && str.charAt(i)<='z') || (str.charAt(i)>='A' && str.charAt(i)<='Z'))
			{
				tmp=str.charAt(i);
			}
			else
			{
				int cnt=Character.getNumericValue(str.charAt(i));
				int j=0;
				while(j<cnt)
				{
					fnl_str=fnl_str+tmp;
					j++;
				}
			}
		}
		return fnl_str;
	}
	
	public static void main(String[] args)
	{
		String str= "aabcccccaaa";
		String tmp=doCompress(str);
		System.out.println("Compressing String: "+tmp);
		System.out.println("Extending String: "+doExtend(tmp));
	}
}
