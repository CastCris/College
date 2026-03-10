/*
 * Esse programa recebe uma nota e verifica se ela é maior que o nescessário para o aluno ser 
 * aprovado
 */
import java.util.Scanner;

public class One
{
    static final double MIN_VAL = 6;

    public static boolean isNumeric(String s)
    {
        int i;
        for(i=0; i < s.length(); ++i){
            if(!Character.isDigit(s.charAt(i))
                    && s.charAt(i) != '.'
                    )
                return false;
        }

        return true;
    }

    public static void main(String args[])
    {
        // /*
        Scanner scan = new Scanner(System.in);
        String inp;
        double val;

        while(true){
            inp = scan.next();
            if(!isNumeric(inp))
                break;

            val = Double.parseDouble(inp);

            if(val < MIN_VAL){
                System.out.println("Nota menor que " + MIN_VAL +". Aluno reprovado");
            }
            else{
                System.out.println("Nota maior ou igual que " + MIN_VAL +". Aluno aprovado");
            }
        }
        // */
    }
}
