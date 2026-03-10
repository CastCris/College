/*
 * Esse programa recebe um ano e verifica se ele é bissexto
 */
import java.util.Scanner;

public class Two
{
    public static boolean isNumeric(String s)
    {
        int i;

        for(i=0; i < s.length(); ++i)
            if(!Character.isDigit(s.charAt(i)))
                return false;

        return true;
    }

    public static void main(String arg[])
    {
        Scanner scan;
        String inp;
        int year;

        scan = new Scanner(System.in);
        while(true){
            inp = scan.next();
            if(!isNumeric(inp))
                break;

            year = Integer.parseInt(inp);
            if(
                    ((year % 4) == 0 && (year % 100) != 0)
                    || (year % 400) == 0
              )
                System.out.println(year + " é um ano bissexto");
            else
                System.out.println(year + " não é um ano bissexto");
        }
    }
}
