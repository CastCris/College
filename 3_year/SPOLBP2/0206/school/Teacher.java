package school;

public class Teacher extends Person
{
    private String _course;
    private double _salary;

    Teacher()
    {
        super();
        this._course = "Undefined";
        this._salary = 0;
    }

    Teacher(String name, int age, String course, double salary)
    {
        super(name, age);
        this._course = course;
        this._salary = salary;
    }

   //
   public String course()
   {
      return this._course;
   }

   public double salary()
   {
       return this._salary;
   }

   //
   public void course_def(String course)
   {
       this._course = course;
   }

   public void salary_def(double salary)
   {
       this._salary = salary;
   }

   //
   public double salary_annual()
   {
       return this._salary * 13;
   }

   @Override
   public String display_infos()
   {
       return "Name: " + this.name() + "\n"
           + "Age: " + this.age() + "\n"
           + "Course: " + this.course() + "\n"
           + "Salary: " + this.salary() + "\n"
           + "Annual salary: " + this.salary_annual() + "\n";
   }
}
