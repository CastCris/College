package packages;

public class Student extends Person
{
    private String _log;
    private double _grade;
    private final static double GRADE_MIN = 6.0;

    Student()
    {
        super();
        this._log = "Undefined";
        this._grade = 0;
    }

    Student(String name, int age, String log, double grade)
    {
        super(name, age);
        this._log = log;
        this._grade = grade;
    }

    //
    public String log()
    {
        return this._log;
    }

    public double grade()
    {
        return this._grade;
    }

    public void log_def(String log)
    {
        this._log = log;
    }

    public void grade_def(double grade)
    {
        this._grade = grade;
    }

    public boolean aproved()
    {
        return this.grade() >= GRADE_MIN;
    }
}
