/*
 * Este programa exibe o ano que você nasceu, considerando que o ano é 2026
 */
import java.util.Scanner;

public class Two
{
    public static void main(String args[])
    {
        final int YEAR = 2026;
        int age;
        Scanner input;

        input = new Scanner(System.in);

        System.out.print("Qual a sua idade?\n");
        age = input.nextInt();

        System.out.printf("Você nasceu em: %d\n", 
                YEAR - age
                );
    }
}
