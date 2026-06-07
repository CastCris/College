import school.StudentCTL;
import school.TeacherCTL;

import java.util.Scanner;
import java.util.regex.Matcher;
import java.util.regex.Pattern;

public class SchoolControl
{
    private static final String
        CMD_EXIT = "EXIT",

        CMD_SEARCH_STUDENT = "SEARCH STUDENT",
        CMD_SEARCH_TEACHER = "SEARCH TEACHER",
        CMD_INSERT_STUDENT = "INSERT STUDENT",
        CMD_INSERT_TEACHER = "INSERT TEACHER",

        CMD_LIST_STUDENT = "LIST STUDENT",
        CMD_LIST_TEACHER = "LIST TEACHER",
        CMD_LIST_ALL = "LIST",

        CMD_HELP = "HELP"
            ;
    private static final Pattern
        PATTERN_EXIT = Pattern.compile(CMD_EXIT, Pattern.CASE_INSENSITIVE),
        PATTERN_SEARCH_STUDENT = Pattern.compile(CMD_SEARCH_STUDENT, Pattern.CASE_INSENSITIVE),
        PATTERN_SEARCH_TEACHER = Pattern.compile(CMD_SEARCH_TEACHER, Pattern.CASE_INSENSITIVE),
        PATTERN_INSERT_STUDENT = Pattern.compile(CMD_INSERT_STUDENT, Pattern.CASE_INSENSITIVE),
        PATTERN_INSERT_TEACHER = Pattern.compile(CMD_INSERT_TEACHER, Pattern.CASE_INSENSITIVE),
        PATTERN_LIST_STUDENT = Pattern.compile(CMD_LIST_STUDENT, Pattern.CASE_INSENSITIVE),
        PATTERN_LIST_TEACHER = Pattern.compile(CMD_LIST_TEACHER, Pattern.CASE_INSENSITIVE),
        PATTERN_LIST_ALL = Pattern.compile(CMD_LIST_ALL, Pattern.CASE_INSENSITIVE),
        PATTERN_HELP = Pattern.compile(CMD_HELP, Pattern.CASE_INSENSITIVE)
            ;
    private static final int
        STUDENT_MAX = 10,
        TEACHER_MAX = 10
            ;

    private static StudentCTL s = new StudentCTL(STUDENT_MAX);
    private static TeacherCTL t = new TeacherCTL(TEACHER_MAX);

    /* */
    public static void main(String args[])
    {
        Scanner scan = new Scanner(System.in);
        String inp;

        System.out.print(
            "Welcome to SchoolControl!" + "\n"
            + "Type commands for manage your schhol! If you is new, type \"HELP\" for more infos about the commands" + "\n"
            );
        do{
            System.out.print("> ");
        }while(loop(inp = scan.nextLine()));
        scan.close();
    }

    public static boolean loop(String cmd)
    {
        if(PATTERN_EXIT.matcher(cmd).find()){
            return loop_exit(cmd);
        }
        else if(PATTERN_SEARCH_STUDENT.matcher(cmd).find()){
            return loop_search_student(cmd);
        }
        else if(PATTERN_SEARCH_TEACHER.matcher(cmd).find()){
            return loop_search_teacher(cmd);
        }
        else if(PATTERN_INSERT_STUDENT.matcher(cmd).find()){
            return loop_insert_student(cmd);
        }
        else if(PATTERN_INSERT_TEACHER.matcher(cmd).find()){
            return loop_insert_teacher(cmd);
        }

        else if(PATTERN_LIST_STUDENT.matcher(cmd).find()){
            return loop_list_student(cmd);
        }
        else if(PATTERN_LIST_TEACHER.matcher(cmd).find()){
            return loop_list_teacher(cmd);
        }
        else if(PATTERN_LIST_ALL.matcher(cmd).find()){
            return loop_list_all(cmd);
        }

        else if(PATTERN_HELP.matcher(cmd).find()){
            return loop_help(cmd);
        }

        else {
            return loop_unknown_cmd(cmd);
        }
    }

    /* */
    private static boolean loop_exit(String cmd)
    {
        System.out.println("Bye!");
        return false;
    }

    private static boolean loop_search_student(String cmd)
    {
        String args, result;

        try{
            args = cmd.split(CMD_SEARCH_STUDENT)[1].trim();
        } catch(Exception e){
            args = "";
        }
        result = s.search_student_from_args(args);
        System.out.println(result);
        return true;
    }
    private static boolean loop_search_teacher(String cmd)
    {
        String args, result;

        try{
            args = cmd.split(CMD_SEARCH_TEACHER)[1].trim();
        } catch(Exception e){
            args = "";
        }
        result = t.search_teacher_from_args(args);
        System.out.println(result);
        return true;
    }
    private static boolean loop_insert_student(String cmd)
    {
        String args, result;

        args = cmd.split(CMD_INSERT_STUDENT)[1].trim();
        result = s.insert_student_from_args(args);
        System.out.println(result);
        return true;
    }
    private static boolean loop_insert_teacher(String cmd)
    {
        String args, result;

        args = cmd.split(CMD_INSERT_TEACHER)[1].trim();
        result = t.insert_teacher_from_args(args);
        System.out.println(result);
        return true;
    }


    private static boolean loop_list_student(String cmd)
    {
        String result;
        result = s.search_student_from_args("{}");
        System.out.println(result);
        return true;
    }
    private static boolean loop_list_teacher(String cmd)
    {
        String result;
        result = t.search_teacher_from_args("{}");
        System.out.println(result);
        return true;
    }
    private static boolean loop_list_all(String cmd)
    {
        String result;
        result = s.search_student_from_args("{}") + "\n" + t.search_teacher_from_args("{}");
        System.out.println(result);
        return true;
    }

    private static boolean loop_help(String cmd)
    {
        System.out.print(
            "General command body: <CMD> <ARGS>\n"
            + "\n"
            + CMD_EXIT + "\n\tdrop the user of program"
            + "\n"
            + "\n"
            + CMD_SEARCH_STUDENT + " {Name=\"String\"|Age=Int|Log=\"String\"|Grade=Double}\n\tSearch for a user in system. You can put one of arguments presets between the braces"
            + "\n"
            + "\n"
            + CMD_SEARCH_TEACHER + " {Name=\"String\"|Age=Int|Course=\"String\"|Salary=Double}\n\tSearch for a teacher in system. You can put one of arugments presents between the braces"
            + "\n"
            + "\n"
            + CMD_INSERT_STUDENT + " {Name=\"String\";Age=Int;Log=\"String\";Grade=Double}\n\tInsert a student in system; The args between braces must be presets"
            + "\n"
            + "\n"
            + CMD_INSERT_TEACHER + " {Name=\"String\";AGe=Int;Course=\"String\";Salary=Double}\n\tInsert a teacher in system; like the above command, the args in braces must be in command"
            + "\n"
            + "\n"
            + CMD_LIST_STUDENT + "\n\tList all students in system"
            + "\n"
            + "\n"
            + CMD_LIST_TEACHER + "\n\tList all teachers in system"
            + "\n"
            + "\n"
            + CMD_LIST_ALL + "\n\tList all students and teachers in system"
            + "\n"
            + "\n"
            + CMD_HELP + "\n\tDisplay this menu"
            + "\n"
            );
        return true;
    }

    private static boolean loop_unknown_cmd(String cmd)
    {
        System.out.print(
            "Unknow command \"" + cmd + "\"\n"
            + "Type " + CMD_HELP + " for more infos about the command\n"
        );
        return true;
    }
}
