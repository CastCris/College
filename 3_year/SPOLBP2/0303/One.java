/*
 * Esse programa recebe um inteiro e verifica se ele é impar ou par
 */
import java.util.Scanner;

    public class One
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
        Scanner s = new Scanner(System.in);
        String input;
        Integer n;

        input = s.next();
        while(isNumeric(input)){
            if(Integer.parseInt(input) % 2 == 0)
                System.out.println("The number " + input + " is even");
            else
                System.out.println("The number " + input + " is odd");

            input = s.next();
        }
    }
}
