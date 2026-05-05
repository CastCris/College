/*
 * Esse arquivo testa a herença java através da classe Animal. Essa classe é herdada pelas
 * classes Cachorro(Dog) e Gato(Cat)
 */
public class One
{
    public static void main(String args[])
    {
        Dog princesinha = new Dog("Princesinha", 10);
        Cat banguela = new Cat("Banguela", 7);

        System.out.println(princesinha.makeSound());
        System.out.println(banguela.makeSound());
    }
}

/* */
public class Animal 
{
    private String name;
    private int age;

    //
    public Animal()
    {
        this.name = "Undefined";
        this.age = 0;
    }

    public Animal(String name, int age)
    {
        this.name = name;
        this.age = age;
    }

    //
        public String makeSound()
    {
        return "Animal Sound";
    }
};

public class Dog extends Animal
{
    public Dog()
    {
        super();
    }

    public Dog(String name, int age)
    {
        super(name, age);
    }

    @Override
    public String makeSound()
    {
        return "Latido";
    }
}

public class Cat extends Animal
{
    public Cat()
    {
        super();
    }

    public Cat(String name, int age)
    {
        super(name, age);
    }

    @Override
    public String makeSound()
    {
        return "Meow";
    }
}
