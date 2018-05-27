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
import java.io.BufferedReader;
import java.io.InputStreamReader;

public class MannasFirstName
{
    public static void main(String args[] ) throws Exception 
    {
        BufferedReader p = new BufferedReader(new InputStreamReader(System.in));    
        int t;
        int suvo,suvojit;
        t = Integer.parseInt(p.readLine());
        String s,sj;
        s = "SUVO";
        sj = "SUVOJIT";
        int i,j,l;
        while(t>0)
        {
            suvo = 0;
            suvojit = 0;
            String str;
            str = p.readLine();
            l = str.length();
            i = str.indexOf(s);
            j = str.indexOf(sj);
            while ( (i >= 0)||(j >= 0))
            {
                //When suvo is existing but is earlier than suvojit
                if ((i<j) && (i!=-1))
                {
                    suvo ++;
                    if(i<l)
                    {
                        i = str.indexOf(s,i+4);
                
                    }
                    else
                    {
                        i = j = -1;
                    }
                }
                //when i and j both points to suvojit.
                //Value of both has to be increased by j+7.
                else if((i==j)&&(i!=-1))
                {
                    suvojit++;
                    if ((j+7)<l)
                    {
                        i = str.indexOf(s,j+7);
                        j = str.indexOf(sj,j+7);
                    }
		    else
		    {
			i = j = -1;
		    }
                }
                else if ((i!=-1)&&(j==-1))
                {
                    suvo++;
                    i = str.indexOf(s,i+4);
                }
            }
        
            System.out.println("SUVO = "+suvo+", SUVOJIT = "+suvojit);
            t--;
        }
    }
}

