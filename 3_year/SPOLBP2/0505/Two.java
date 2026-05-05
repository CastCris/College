public class Main
{
    public static void main(String args[])
    {
        Car focus = new Car("ford", "focus", 4);
        Moto moto = new Moto("moto", "22222", 10000);

        System.out.println(focus.toString());
        System.out.println(moto.toString());
    }
}

/* */
public class Vehile
{
    private String marca;
    private String modelo;

    public Vehile()
    {
        this.marca = "";
        this.modelo = "";
    }

    public Vehile(String marca, String modelo)
    {
        this.marca = marca;
        this.modelo = modelo;
    }

    //
    public void turnOn()
    {
    }

    public void turnOff()
    {
    }

    public String toString()
    {
        return 
            "marca: " + this.marca + "\n"
            + "modelo: " + this.modelo + "\n";
    }
}

public class Car extends Vehile
{
    public int doors_amt;
    
    public Car()
    {
        super();
        this.doors_amt = 0;
    }

    public Car(String marca, String modelo, int doors_amt)
    {
        super(marca, modelo);
        this.doors_amt = doors_amt;
    }

    @Override
    public String toString()
    {
        return 
            super.toString()
            + "potas: " + this.doors_amt + "\n";
    }
}

public class Moto extends Vehile
{
    public int cilindradas;

    public Moto()
    {
        super();
        this.cilindradas = 0;
    }

    public Moto(String marca, String modelo, int cilindradas)
    {
        super(marca, modelo);
        this.cilindradas = cilindradas;
    }

    @Override
    public String toString()
    {
        return
            super.toString()
            + "cilindradas: " + this.cilindradas + "\n";
    }
}
