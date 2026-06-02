package packages;

public class Person
{
    private String _name;
    private int _age;

    public Person()
    {
        this._name = "Undefined";
        this._age = 0;
    }

    public Person(String name, int age)
    {
        this._name = name;
        this._age = 0;
    }

    //
    public String name()
    {
        return this._name;
    }

    public int age()
    {
        return this._age;
    }

    public void name_def(String name)
    {
        this._name = name;
    }

    public void age_def(int age)
    {
        this._age = age;
    }

    //
    public void display_infos()
    {
        System.out.println(
            "Name: " + this.name() + "\n"
            + "Age: " + this.age() + "\n"
        );
    }
}
