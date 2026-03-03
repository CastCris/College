/*
 * Esse programa lê pares separados por espaço e verifica se os valores são iguais ou diferentes
 */

import java.util.Scanner;

public class Three
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
        Scanner scan = new Scanner(System.in);
        String input;
        String[] n = new String[2];
        int i;

        i = 0;
        while(true){
            input = scan.next();
            if(!isNumeric(input))
                break;

            n[i++] = input;
            if(i < 2)
                continue;

            if(Integer.parseInt(n[0]) != Integer.parseInt(n[1]))
                System.out.println(n[0] + " != " + n[1]);
            else
                System.out.println(n[0] + " == " + n[1]);

            i %= 2;
        }
    }
}
