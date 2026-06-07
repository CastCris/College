package school;
import java.util.regex.Pattern;

public class StudentCTL
{
    private Student students[];
    // /*
    private static final Pattern 
        PATTERN_ARGS_BRACE = Pattern.compile("\\{*\\}");
        // */
    private int students_i;
    private int students_size;

    public StudentCTL(int students_size)
    {
        this.students = new Student[students_size];
        this.students_i = 0;
        this.students_size = students_size;
    }

    public String insert_student_from_args(String args)
    {
        if(!PATTERN_ARGS_BRACE.matcher(args).find()){
            return "Invalid argument line: Missing braces";
        }

        String args_f = args;
        if(args_f.split(";").length != 4){
            return "Invalid number of arguments";
        }
        args_f = args_f.split("\\{")[1].split("\\}")[0].trim();

        String errors = "";
        String name="", log="";
        int age=0;
        double grade=0;
        // Name
        try {
            name = args_f.split("Name=")[1].split(";")[0].trim();
        }
        catch(ArrayIndexOutOfBoundsException e){
            errors += "Missing \"Name\" argument\n";
        }

        // Age
        try {
            age = Integer.parseInt(args_f.split("Age=")[1].split(";")[0].trim());
        }
        catch(ArrayIndexOutOfBoundsException e){
            errors += "Missing \"Age\" argument\n";
        }
        catch(NumberFormatException e){
            errors += "Invalid \"Age\" number format\n";
        }
        finally {
            if(age < 0){
                errors += "Invalid numeric value for \"Age\" argument\n";
            }
        }
        
        // Log
        try {
            log = args_f.split("Log=")[1].split(";")[0].trim();
        }
        catch(ArrayIndexOutOfBoundsException e){
            errors += "Missing \"Log\" argument\n";
        }

        // Grade
        try {
            grade = Double.parseDouble(args_f.split("Grade=")[1].split(";")[0].trim());
        }
        catch(ArrayIndexOutOfBoundsException e){
            errors += "Missing \"Grade\" argument\n";
        }
        catch(NumberFormatException e){
            errors += "Invalid \"Grade\" number format\n";
        }
        finally {
            if(grade < 0 || grade > 10){
                errors += "Invalid numeric value for \"Grade\" argument\n";
            }
        }

        if(this.students_i >= this.students_size){
            errors += "Max student reached\n";
        }

        if(errors.length() == 0){
            this.students[this.students_i++] = new Student(name, age, log, grade);
            errors = "Insertion peformed with success!";
        }
        return errors; 
    }

    public String search_student_from_args(String args)
    {
        if(!PATTERN_ARGS_BRACE.matcher(args).find()){
            return "Invalid argument line: Missing braces";
        }

        String args_f = "";
        try{
            args_f = args.split("\\{")[1].split("\\}")[0];
        }
        catch(Exception e){
        }

        String name_rgx, age_rgx, log_rgx, grade_rgx;
        name_rgx = age_rgx = log_rgx = grade_rgx = ".*";
        // System.out.println(args_f);

        // Name
        try {
            name_rgx = args_f.split("Name=")[1].split(";")[0];
        } 
        catch(Exception e){
        }

        // Age
        try {
            age_rgx = args_f.split("Age=")[1].split(";")[0];
        }
        catch(Exception e){
        }

        // Log
        try {
            log_rgx = args_f.split("Log=")[1].split(";")[0];
        }
        catch(Exception e){
        }

        // Grade
        try {
            grade_rgx = args_f.split("Grade=")[1].split(";")[0];
        }
        catch(Exception e){
        }
        // System.out.println(name_rgx);

        //
        Pattern name_ptrn, age_ptrn, log_ptrn, grade_ptrn;
        name_ptrn = Pattern.compile(name_rgx, Pattern.CASE_INSENSITIVE);
        age_ptrn = Pattern.compile(age_rgx, Pattern.CASE_INSENSITIVE);
        log_ptrn = Pattern.compile(log_rgx, Pattern.CASE_INSENSITIVE);
        grade_ptrn = Pattern.compile(grade_rgx, Pattern.CASE_INSENSITIVE);

        String result;
        Student s;
        int result_i;

        result = "";
        result_i = 0;
        for(int i=0; i < this.students_i; ++i){
            s = this.students[i];
            if(
                name_ptrn.matcher(s.name()).find()
                && age_ptrn.matcher(String.valueOf(s.age())).find()
                && log_ptrn.matcher(s.log()).find()
                && grade_ptrn.matcher(String.valueOf(s.grade())).find()
            ){
                result += s.display_infos();
                result += "===============\n";
                ++result_i;
            }
        }

        if(result.length() == 0){
            result = "<EMPTY QUERY>\n";
        }
        result += "Amount queries: " + result_i;

        return result;
    }
}
