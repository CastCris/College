/*
 * Esse programa recebe pares de números, separados por vírgula(,), e diz se o primeiro número
 * do par é maior ou menor que o último número do par
 */
import java.util.Scanner;

public class Two
{
    public static boolean isNumeric(String s)
    {
        int i;

        for(i=0; i < s.length(); ++i){
            if(!Character.isDigit(s.charAt(i)))
                return false;
        }

        return true;
    }

    public static void main(String args[])
    {
        Scanner scan_pair = new Scanner(System.in).useDelimiter(",|\n");
        Scanner scan_int;
        String input;
        String n1, n2;

        while(true){
            input = scan_pair.next();
            scan_int = new Scanner(input);
            
            n1 = scan_int.next();
            n2 = scan_int.next();

            if(!isNumeric(n1) || !isNumeric(n2))
                break;

            if(Integer.parseInt(n1) <= Integer.parseInt(n2))
                System.out.println(n1 + " <= " + n2);
            else
                System.out.println(n1 + " > " + n2);

            scan_int.close();
        }

        scan_pair.close();
    }
}
