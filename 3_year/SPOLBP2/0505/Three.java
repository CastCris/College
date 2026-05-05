public class Three
{
    public static void main(String args[])
    {
    }
}

//
public class LibraryItem
{
    private String title;
    private int yearPublication;
    
    public LibraryItem()
    {
        this.title = "";
        this.yearPublication = 0;
    }

    public LibraryItem(String title, int year)
    {
        this.title = title;
        this.yearPublication = year;
    }

    //
    public String infos()
    {
        return "título: " + this.title + "\n"
            + "Ano de publicação: " + this.yearPublication + "\n";
    }

    public String toString()
    {
        return this.infos();
    }

    public boolean equals(LibraryItem a)
    {
        return this.title == a.title
            && this.yearPublication == a.yearPublication;
    }
}

public class Book extends LibraryItem
{
    private String author;

    public Book()
    {
        super();
        this.author = "";
    }

    public Book(String title, int year, String author)
    {
        super(title, year);
        this.author = author;
    }

    //
    @Override
    public String infos()
    {
        return super.infos() + "\n"
            + "Autor: " + this.author + "\n";
    }

    public boolean equals(Book a)
    {
        return super.equals(a)
            && this.author = a.author;
    }
}

public class Magazine extends LibraryItem
{
    private String edition;

    public Magazine()
    {
        super();
        this.edition = "";
    }

    public Magazine(String title, int year, String edition)
    {
        super(title, year);
        this.edition = edition;
    }

    //
    @Override
    public String infos()
    {
        return super.infos() + "\n"
            + "Edition: " + this.edition + "\n";
    }

    public boolean equals(Magazine a)
    {
        return super.equals(a)
            && this.edition = a.edition;
    }
}
