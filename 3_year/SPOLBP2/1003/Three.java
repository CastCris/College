/*
 * Esse programa recebe uma quantidade N de número e retorna o maior
 */
import java.util.Scanner;

public class Three
{
    public static boolean isNumeric(String s)
    {
        int i;
        for(i=0; i < s.length(); ++i)
            if(
                    !Character.isDigit(s.charAt(i))
                    && s.charAt(i) != '.'
                    )
                return false;
        return true;
    }

    public static void main(String args[])
    {
        Scanner scan;
        String inp;
        double val, max;

        scan = new Scanner(System.in);
        max = 0;
        while(
                isNumeric((inp = scan.next()))
             ){
            val = Double.parseDouble(inp);
            if(val > max)
                max = val;
        }

        System.out.println("Valor máximo recebido " + max);
    }
}
