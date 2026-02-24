/*
 * Constante velocidade deve ser atribuída ao tipo int
 * Constante meses_do_ano deve ser atribuído ao tipo int
 * Constante PI deve ser atribuído ao tipo double
 */

public class Five
{
    public static void main(String args[])
    {
        final int MAX_SPEED = 80;
        final int MOUNTH_IN_YEAR = 12;
        final double PI = 3.14159;

        System.out.printf(
            "Velocidade máxima na via: %d\nMeses no ano: %d\nValor de pi: %.5f\n", 
            MAX_SPEED, MOUNTH_IN_YEAR, PI
        );
    }
}
