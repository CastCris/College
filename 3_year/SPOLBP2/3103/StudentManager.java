/*
 * This program is a student manager / control.
 * Using it, you can insert, remove, update and query the student through of student's attributes,
 * like id, age, name, class etc.
 */
import java.util.Scanner;
import java.util.HashMap;
import java.time.LocalDateTime;

/* Main  */
public class StudentManager
{
    static final short SCREEN_WIDTH = 50;
    static final short SCREEN_HEIGH = 2;

    static Menu menu = Menu.WELCOME;
    static System_User sys_u = new System_User();
    static System_Student sys_s = new System_Student();

    static Scanner scan = new Scanner(System.in);

    //
    public static void menuWelcome()
    {
        System.out.println("WELCOME!");
        
        int i;
        for(i=0; i < SCREEN_WIDTH; ++i){
            System.out.print("*");
        }
        System.out.println();
    }

    public static void menuLogin()
    {
        int userId;
        String userPass;

        System.out.println("LOGIN");
        System.out.print("Enter with user's id: ");
        userId = scan.nextLine();

        System.out.print("Enter with user's password: ");
        userPass = scan.nextLine();

        if(sys_u.user_valid(userId, userPass)){
        }
    }



    //
    public static void loop()
    {
        switch(menu){
            case Menu.WELCOME:
                menuWelcome();
                menu = Menu.LOGIN;

                break;

            case Menu.LOGIN:
                menuLogin();
        }
    }

    public static void main(String args[])
    {
        while(true){
            loop();
        }
    }
};


/* System */
class System_User
{
    static final short MAX_USER = 50;
    private static User[] users;

    public System_User()
    {
        this.users = new User[MAX_USER];

        user_insert(new User(10, "abcd"));
    }

    //
    private static User get_user(int id)
    {
        int i;
        for(i=0; i < MAX_USER && users[i] != null; ++i){
             if(users[i].id() == id)
                return users[i];
        }

        return null;
    }


    public static boolean user_valid(int id)
    {
        return get_user(id) != null;
    }

    public static boolean user_auth(int id, String password)
    {
        User user = get_user(id);
        if(user == null)
            return false;

        return user.password() == password;
    }

    
    public static boolean user_insert(User u)
    {
        int i;
        for(i=0; i < MAX_USER && users[i] != null; ++i);

        if(i == MAX_USER){
            return false;
        }

        users[i] = u;
        return true;
    }
}

class System_Student
{
    static final short MAX_STUDENTS = 1000;
    static Student[] systemStudents = new Student[MAX_STUDENTS];
}

/* */
enum Menu {
    STUDENT_INSERT,
    STUDENT_REMOVE,
    STUDENT_UPDATE,
    STUDENT_SEARCH,

    /*
    ATTR_STUDENT_INSERT,
    ATTR_STUDENT_REMOVE,
    ATTR_STUDENT_UPDATE,
    ATTR_STUDENT_SEARCH,
    // */

    LOGIN,
    SIGN,
    WELCOME
};

//
class Student
{
    int _id;

    String _name;
    short _age;
    double _grade;
};

class User
{
    private int _id;
    private String _password;

    public User(int id, String pass)
    {
        this._id = id;
        this._password = pass;
    }

    //
    public int id()
    {
        return this._id;
    }

    public String password()
    {
        return this._password;
    }
}
