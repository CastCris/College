/*
 * Esse programa recebe uma string e le os carácters dela e informa se eles são vogais, consoantes ou
 * nenhum dos dois
 */
import java.util.Scanner;

public class Four
{
    public static char[] vogals = {'a', 'e', 'i', 'o', 'u'};

    public static int IS_VOGAL = 0;
    public static int ISNT_VOGAL = 1;
    public static int ISNT_ALPHA = 2;

    //
    public static int isVogal(char c)
    {
        if(!Character.isAlphabetic(c))
            return ISNT_ALPHA;

        int i;
        for(i=0; i < vogals.length; ++i)
            if(vogals[i] == c)
                return IS_VOGAL;

        return ISNT_VOGAL;
    }

    public static void main(String args[])
    {
        Scanner scan;
        String s;
        int i, cVogal;
        char c;

        scan = new Scanner(System.in);
        while(true){
            s = scan.next();

            for(i=0; i < s.length(); ++i){
                c = s.charAt(i);
                cVogal = isVogal(c);

                if(cVogal == IS_VOGAL){
                    System.out.println(c + " é vogal");
                }
                else if(cVogal  == ISNT_VOGAL){
                    System.out.println(c + " não é vogal");
                }
                else if(cVogal == ISNT_ALPHA){
                    System.out.println(c + " não faz parte do alfabeto");
                }
            }
        }
    }
}
