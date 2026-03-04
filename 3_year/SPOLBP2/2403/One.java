/*
 * Este programa recebe, armazena e exibe os valores nomes, idade e tamanho se você fosse um surfista!
 */
import java.util.Scanner;

public class One
{
    public static void main(String[] args)
    {
        String name;
        int age;
        double height;

        Scanner input = new Scanner(System.in);

        //
        System.out.print("Entre com o seu nome de surfista: ");
        name = input.nextLine();

        System.out.print("Entre com a sua idade de surfista: ");
        age = input.nextInt();

        System.out.print("Entre com a sua altura(m) de surfista: ");
        height = input.nextDouble();

        System.out.printf("Seus dados de surfista:\nNome:%s\nIdade:%d\nAltura:%.2f\n",
                name,
                age,
                height
                );
    }
}
