/*
 * Esse programa recebe um double e verifica se ele é maior ou menor que 100
 */

import java.util.Scanner;

public class Four
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

    public static void main()
    {
        Scanner s = System
