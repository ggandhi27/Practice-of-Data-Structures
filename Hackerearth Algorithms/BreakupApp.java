/* IMPORTANT: Multiple classes and nested static classes are supported */

/*
 * uncomment this if you want to read input.
//imports for BufferedReader
import java.io.BufferedReader;
import java.io.InputStreamReader;

//import for Scanner and other utility classes
import java.util.*;
*/

// Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
import java.util.*;
import java.io.*;
public class BreakupApp {
    public static void main(String args[] ) throws Exception 
    {
        int n;
        BufferedReader p = new BufferedReader(new InputStreamReader(System.in));
        int arr[] = new int[31];
        n = Integer.parseInt(p.readLine());
        String str;
        int f,i,l;
	String s;
        char ch;
        int max;
        max = 0;
        while (n>0)
        {
            n--;
            str = p.readLine();
            f = 0;
            if(str.charAt(0)=='G')
            {
                f = 1;
            }
            else
            {
                f = 2;
            }
            l = str.length();
            i = 1;
            while(i<l)
            {
                ch = str.charAt(i);
                if((ch >= '0') && (ch <= '9'))
                {
			s = "";
			while(i<l)
			{
				ch = str.charAt(i);
				if(!((ch>='0')&&(ch<='9')))
				{
					break;
				}
				else
				{
					s=s+ch;
				}
				
				i++;	
			}
			int a = Integer.parseInt(s);
			if (f == 1)
			{
				arr[a] = arr[a]+2;
			}
			else
			{
				arr[a]++;
			}
			if (arr[max]<arr[a])
			{
				max = a;
			}
			continue;
		}
		i++;
            }
            
        }
        if ((max == 19)||(max == 20))
            {
                System.out.println("Date");
            }
            else
            {
                System.out.println("No Date");
            }
    }
}

