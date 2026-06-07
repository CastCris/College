package school;
import java.util.regex.Pattern;

public class TeacherCTL
{
    private Teacher teachers[];
    private int teachers_i;
    private int teachers_size;
    private static final Pattern
        PATTERN_ARGS_BRACE = Pattern.compile("\\{*\\}");


    public TeacherCTL(int teachers_size)
    {
        this.teachers = new Teacher[teachers_size];
        this.teachers_i = 0;
        this.teachers_size = teachers_size;
    }

    public String insert_teacher_from_args(String args)
    {
        if(!PATTERN_ARGS_BRACE.matcher(args).find()){
            return "Invalid command: Missing braces";
        }

        String args_f;
        args_f = args.split("\\{")[1].split("\\}")[0].trim();
        if(args_f.split(";").length != 4){
            return "Invalid number of arguments";
        }

        String errors;
        String name, course;
        int age;
        double salary;

        name = course = errors = "";
        age = 0;
        salary = 0;
        // Name
        try {
            name = args_f.split("Name=")[1].split(";")[0];
        }
        catch(ArrayIndexOutOfBoundsException e){
            errors += "Missing \"Name\" argument\n";
        }

        // Age
        try {
            age = Integer.parseInt(args_f.split("Age=")[1].split(";")[0]);
        }
        catch(ArrayIndexOutOfBoundsException e){
            errors += "Missing \"Age\" argument\n";
        }
        catch(NumberFormatException e){
            errors += "Invalid \"Age\" number format\n";
        }

        // Couse
        try {
            course = args_f.split("Course=")[1].split(";")[0];
        }
        catch(ArrayIndexOutOfBoundsException e){
            errors += "Missing \"Couse\" argument\n";
        }

        // Salary
        try {
            salary = Double.parseDouble(args_f.split("Salary=")[1].split(";")[0]);
        }
        catch(ArrayIndexOutOfBoundsException e){
            errors += "Missing \"Salary\" argument\n";
        }
        catch(NumberFormatException e){
            errors += "Invalid \"Salary\" number format";
        }

        if(this.teachers_i >= this.teachers_size){
            errors += "Max teachers reached";
        }

        if(errors.length() == 0){
            this.teachers[this.teachers_i++] = new Teacher(name, age, course, salary);
            errors = "Insertion peformed with success!";
        }

        return errors;
    }

    public String search_teacher_from_args(String args)
    {
        if(!PATTERN_ARGS_BRACE.matcher(args).find()){
            return "Invalid command: Missing braces";
        }

        String args_f;
        try{
            args_f = args.split("\\{")[1].split("\\}")[0];
        }
        catch(Exception e){
            args_f = "";
        }

        String name, age, course, salary;
        name = age = course = salary = ".*";
        // Name
        try {
            name = args_f.split("Name=")[1].split(";")[0];
        }
        catch(Exception e){
        }

        // Age
        try {
            age = String.valueOf(args_f.split("Age=")[1].split(";")[0]);
        }
        catch(Exception e){
        }

        // Course
        try {
            course = args_f.split("Couse=")[1].split(";")[0];
        }
        catch(Exception e){
        }

        // Salary
        try {
            salary = String.valueOf(args_f.split("Salary=")[1].split(";")[0]);
        }
        catch(Exception e){
        }

        Pattern p_name, p_age, p_course, p_salary;
        p_name = Pattern.compile(name, Pattern.CASE_INSENSITIVE);
        p_age = Pattern.compile(name, Pattern.CASE_INSENSITIVE);
        p_course = Pattern.compile(name, Pattern.CASE_INSENSITIVE);
        p_salary = Pattern.compile(name, Pattern.CASE_INSENSITIVE);
        int i;
        Teacher t;
        String result = ""; 
        for(i=0; i < this.teachers_i; ++i){
            t = this.teachers[i];
            if(
                 p_name.matcher(t.name()).find()
                 && p_age.matcher(String.valueOf(t.age())).find()
                 && p_course.matcher(t.course()).find()
                 && p_salary.matcher(String.valueOf(t.salary())).find()
              ){
                 result += t.display_infos();
                 result += "===============\n";
              }
        }

        if(result.length() == 0){
            result = "<EMPTY QUERIE>\n";
        }
        result += "Amount queries: " + i;

        return result;
    }
}
