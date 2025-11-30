
class Book():
    def __init__(self, title:str, author:str, pages:int)->None:
        self.title = title
        self.author = author
        self.pages = pages

    def __repr__(self)->str:
        return f"""
        Title: {self.title};
        Author: {self.author};
        Pages: {self.pages}.
        """

instance = Book(
    title = "O Guarani",
    author = "Jose de Alencar",
    pages = 342
)

print(instance)
