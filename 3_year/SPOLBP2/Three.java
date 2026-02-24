/*
 * A saída do código será 10, pois à variável b é atribuído a, que armazena 10, que logo após é
 * atribuído ao mesmo 20
 */

public class Three
{
    public static void main(String args[])
    {
        int a, b;

        a = 10;
        b = a;
        a = 20;

        System.out.println(b);
    }
}
