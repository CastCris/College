/*
 * This program is a student manager / control.
 * Using it, you can insert and search students.
 *
 *
 */
import java.util.Scanner;
import java.time.LocalDateTime;
import java.time.format.DateTimeFormatter;

class StudentManager
{
    static final String CMD_HELP = "HELP";
    static final String CMD_INSERT_STUDENT = "INSERT STUDENT";
    static final String CMD_SEARCH_STUDENT = "SEARCH STUDENT";
    static final String CMD_SYS_INFOS = "SYS INFOS";
    static final String CMD_EXIT = "EXIT";
    static final DateTimeFormatter date_formatter = 
        DateTimeFormatter.ofPattern("dd/MMM/yy HH:mm:ss, E");

    static Menu menu = Menu.BOOT;
    static Menu menu_last;
    static boolean menu_swapped = false;

    static Scanner scan = new Scanner(System.in);

    //
    private static void loop()
    {
        menu_last = menu;

        switch(menu){
            case Menu.BOOT:
                menu_boot();
                break;

            case Menu.HELP:
                menu_help();
                break;

            case Menu.HELP_INSERT_STUDENT:
                menu_help_insertStudent();
                break;

            case Menu.HELP_SEARCH_STUDENT:
                menu_help_searchStudent();
                break;


            case Menu.PROMPT:
                menu_prompt();
                break;

            case Menu.INSERT_STUDENT:
                menu_insert();
                break;

            case Menu.SEARCH_STUDENT:
                menu_search();
                break;

            case Menu.SYS_INFOS:
                menu_sysInfos();
                break;


            case Menu.EXIT_INSERT_STUDENT:
                menu_exit_insertStudent();
                break;

            case Menu.EXIT_SEARCH_STUDENT:
                menu_exit_searchStudent();
                break;

            case Menu.EXIT_PROMPT:
                menu_exit();
                break;

            default:
                break;
        }

        menu_swapped = menu_last != menu;
    }

    public static void main(String args[])
    {
        while(true){
            loop();
            if(menu == Menu.END)
                break;
        }
    }


    private static void menu_boot()
    {
        System.out.print(
                String.format(
                "WELCOME TO STUDENT MANAGER!"
                + "\n"
                + "***************************"
                + "\n"
                + "Type \"%s\" for more infos"
                + "\n",

                CMD_HELP
                )
        );


        menu = Menu.PROMPT;
    }

    private static void menu_help()
    {
        System.out.print(
                String.format(
                "-----------\n"
                + "Type: "
                + "\n"
                + "\"%s\" for view this menu"

                + "\n"
                + "\"%s\" for enter into insert student menu"

                + "\n"
                + "\"%s\" for enter into search student menu"

                + "\n"
                + "\"%s\" for view system infos"

                + "\n"
                + "\"%s\" for exit of program"
                + "\n"
                + "-----------\n"
                ,

                CMD_HELP,
                CMD_INSERT_STUDENT,
                CMD_SEARCH_STUDENT,
                CMD_SYS_INFOS,
                CMD_EXIT
                )
        );

        menu = Menu.PROMPT;
    }

    private static void menu_help_insertStudent()
    {
        System.out.print(
                String.format(
                "Put the student attributes into form: "
                + "\n"
                + "Id(Int), Name(String), Age(Int), Grade(Dobule)"
                + "\n",

                CMD_HELP
                )
        );

        menu = Menu.INSERT_STUDENT;
    }

    private static void menu_help_searchStudent()
    {
        System.out.print(
                String.format(
                "Type: "
                + "\n"
                + "\"%s, ARGS\" for search student by id, where id = ARGS"
                + "\n"
                + "\"%s, ARGS\" for search student by name, where name = ARGS"
                + "\n"
                + "\"%s, ARGS\" for search student by age, where age = ARGS"
                + "\n"
                + "\"%s\" for get the average age of all students"
                + "\n"
                + "\"%s\" for get all students"
                + "\n",

                Sys_Students.SEARCH_BY_ID,
                Sys_Students.SEARCH_BY_NAME,
                Sys_Students.SEARCH_BY_AGE,
                Sys_Students.SEARCH_AVERAGE_AGE,
                Sys_Students.SEARCH_ALL,
                CMD_HELP
                )
        );

        menu = Menu.SEARCH_STUDENT;
    }


    private static void menu_prompt()
    {
        System.out.print("> ");

        String command = scan.nextLine().toUpperCase().trim();

        if(command.equals(CMD_HELP)){
            menu = Menu.HELP;
        }
        else if(command.equals(CMD_INSERT_STUDENT)){
            menu = Menu.INSERT_STUDENT;
        }
        else if(command.equals(CMD_SEARCH_STUDENT)){
            menu = Menu.SEARCH_STUDENT;
        }
        else if(command.equals(CMD_SYS_INFOS)){
            menu = Menu.SYS_INFOS;
        }
        else if(command.equals(CMD_EXIT)){
            menu = Menu.EXIT_PROMPT;
        }
        else {
            System.out.println("COMMAND NOT FOUND");
        }
    }

    private static void menu_insert()
    {
        if(menu_swapped)
            System.out.println(
                    String.format(
                        "Type \"%s\" for more info about this menu",
                        CMD_HELP
                    )
            );

        System.out.print("i > ");

        String arg;
        arg = scan.nextLine().trim();
        if(arg.toUpperCase().equals(CMD_EXIT)){
            menu = Menu.EXIT_INSERT_STUDENT;
            return;
        }
        else if(arg.equals(CMD_HELP)){
            menu = Menu.HELP_INSERT_STUDENT;
            return;
        }

        Sys_Students.insert_by_str(arg);
    }

    private static void menu_search()
    {
        if(menu_swapped)
            System.out.println(
                    String.format(
                        "Type \"%s\" for more info about this menu",
                        CMD_HELP
                    )
            );

        System.out.print("s > ");

        String cmd = scan.nextLine().trim();
        if(cmd.toUpperCase().equals(CMD_EXIT)){
            menu = Menu.EXIT_SEARCH_STUDENT;
            return;
        }
        else if(cmd.toUpperCase().equals(CMD_HELP)){
            menu = Menu.HELP_SEARCH_STUDENT;
            return;
        }

        Student[] result;
        result = Sys_Students.search_by_cmd(cmd);

        for(Student i: result){
            if(i == null)
                break;

            i.print();
        }
    }

    private static void menu_sysInfos()
    {
        System.out.print(
                "System Infos"
                + "\n"
                + "------------"
                + "\n"
                + "Date: " + LocalDateTime.now().format(date_formatter)
                + "\n"
                + "Students into system: " + Sys_Students.students_in_sys()
                + "\n"
                + "------------"
                + "\n"
        );

        menu = Menu.PROMPT;
    }

    private static void menu_exit()
    {
        System.out.println(
                "Bye!"
                );

        menu = Menu.END;
    }

    private static void menu_exit_insertStudent()
    {
        menu = Menu.PROMPT;
    }

    private static void menu_exit_searchStudent(){
        menu = Menu.PROMPT;
    }
}

/* */
enum Loop {
    FINISH
};

enum Menu {
    BOOT,
    HELP,
    HELP_INSERT_STUDENT,
    HELP_SEARCH_STUDENT,

    PROMPT,
    INSERT_STUDENT,
    SEARCH_STUDENT,
    SYS_INFOS,

    EXIT_INSERT_STUDENT,
    EXIT_SEARCH_STUDENT,
    EXIT_PROMPT,

    END
};

enum StudentCrud {
    SEARCH_BY_ID,
    SEARCH_BY_NAME,
    SEARCH_BY_AGE,
    SEARCH_ALL,
    SEARCH_AVERAGE_AGE,

    INVALID_CRUD
};

/* */
class Sys_Students
{
    private static final int _STUDENTS_MAX = 5;

    private static final String _SEARCH_PREFIX = "SEARCH";
    private static final String _INSERT_PREFIX = "INSERT";
    private static final String _BLANK = " ";

    public static final String SEARCH_BY_ID =
        _SEARCH_PREFIX + _BLANK + "ID";
    public static final String SEARCH_BY_NAME =
        _SEARCH_PREFIX + _BLANK + "NAME";
    public static final String SEARCH_BY_AGE =
        _SEARCH_PREFIX + _BLANK + "AGE";
    public static final String SEARCH_AVERAGE_AGE =
        _SEARCH_PREFIX + _BLANK + "AVERAGE AGE";
    public static final String SEARCH_ALL =
        _SEARCH_PREFIX;


    public static Student[] s = new Student[_STUDENTS_MAX];
    private static int s_size = 0;

    //
    public static void insert(Student s_new)
    {
        if(s_size >= _STUDENTS_MAX)
            return;

        int i;
        for(i=0; i < s_size; ++i){
            if(s[i].id == s_new.id)
                return;
        }

        s[s_size++] = s_new;
    }

    public static void insert_by_str(String arg)
    {
        String[] args = arg.split(",");
        int id;
        String name;
        int age;
        double grade;

        //
        id = Integer.parseInt(args[0].trim());
        name = args[1].trim();
        age = Integer.parseInt(args[2].trim());
        grade = Double.parseDouble(args[3].trim());

        Student t = new Student(id, name, age, grade);
        insert(t);
    }


    public static Student[] search_by_queryType(
            StudentCrud queryType, String query_arg
            )
    {
        switch(queryType){
            case StudentCrud.SEARCH_BY_ID:
                return _search_by_id(Integer.parseInt(query_arg));

            case StudentCrud.SEARCH_BY_NAME:
                return _search_by_name(query_arg);

            case StudentCrud.SEARCH_BY_AGE:
                return _search_by_age(Integer.parseInt(query_arg));

            case StudentCrud.SEARCH_AVERAGE_AGE:
                return _search_average_age();

            case StudentCrud.SEARCH_ALL:
                return _search_all();

            case StudentCrud.INVALID_CRUD:
                return _search_error();

            default:
                return s;
        }
    }

    public static Student[] search_by_cmd(String cmd)
    {
        StudentCrud queryType;
        String[] splited_cmd;
        String query, args;

        splited_cmd = cmd.split(",");
        query = splited_cmd[0].trim();
        args = "";
        if(splited_cmd.length > 1)
            args = splited_cmd[1].trim();

        System.out.println(args);
        queryType = _query_type(query);
        return search_by_queryType(queryType, args);
    }


    public static int students_in_sys()
    {
        return s_size;
    }

    //
    private static Student[] _search_by_id(int id)
    {
        Student result[] = new Student[_STUDENTS_MAX];
        int result_size = 0;

        int i;
        for(i=0; i < s_size; ++i){
            if(s[i].id == id)
                result[result_size++] = s[i];
        }

        return result;
    }

    private static Student[] _search_by_name(String name)
    {
        Student result[] = new Student[_STUDENTS_MAX];
        int result_size = 0;

        int i;
        for(i=0; i < s_size; ++i){
            if(s[i].name.equals(name))
                result[result_size++] = s[i];
        }

        return result;
    }

    private static Student[] _search_by_age(int age)
    {
        Student result[] = new Student[_STUDENTS_MAX];
        int result_size = 0;

        int i;
        for(i=0; i < s_size; ++i){
            if(s[i].age == age)
                result[result_size++] = s[i];
        }

        return result;
    }

    private static Student[] _search_average_age()
    {
        Student[] result = { new Student(0, "Result Avegrage", 0, 0) };

        int i;
        for(i=0; i < s_size; ++i){
            result[0].age += s[i].age;
        }

        result[0].age /= s_size;
        return result;
    }

    private static Student[] _search_all()
    {
        return s;
    }

    private static Student[] _search_error()
    {
        Student[] result = { new Student(0, "Error in query", 0, 0) };
        return result;
    }


    private static StudentCrud _query_type(String query)
    {
        if(query.equals(SEARCH_BY_ID)){
            return StudentCrud.SEARCH_BY_ID;
        }
        else if(query.equals(SEARCH_BY_NAME)){
            return StudentCrud.SEARCH_BY_NAME;
        }
        else if(query.equals(SEARCH_BY_AGE)){
            return StudentCrud.SEARCH_BY_AGE;
        }

        else if(query.equals(SEARCH_AVERAGE_AGE)){
            return StudentCrud.SEARCH_AVERAGE_AGE;
        }
        else if(query.equals(SEARCH_ALL)){
            return StudentCrud.SEARCH_ALL;
        }

        else{
            return StudentCrud.INVALID_CRUD;
        }
    }
}

class Student
{
    int id;
    int age;
    String name;
    double grade;

    static final String PRINT_LINE_SEPARATOR = "\n--------------------\n";
    static final String PRINT_DELIMITER = "\n====================\n";

    //
    public Student(int id, String name, int age, double grade)
    {
        this.id = id;
        this.name = name;
        this.age = age;
        this.grade = grade;
    }

    public void print()
    {
        System.out.print(
                PRINT_DELIMITER
                + "ID:    " + this.id 
                + PRINT_LINE_SEPARATOR
                + "NAME:  " + this.name
                + PRINT_LINE_SEPARATOR
                + "AGE:   " + this.age
                + PRINT_LINE_SEPARATOR
                + "GRADE: " + this.grade
                + PRINT_DELIMITER
        );
    }
}
