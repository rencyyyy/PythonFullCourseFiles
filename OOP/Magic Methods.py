# MAGIC METHODS - Dunder methods (double underscore) __init__, __str__, __eq__
#                 They are automatically called by many of Python's built-in operations.
#                 They allow developers to define or customize the behavior of objects

class Book:

    def __init__(self, title, author, num_pages):
        self.title = title
        self.author = author
        self.num_pages = num_pages

    def __str__(self):
        return f"'{self.title}' by {self.author}"

    def __eq__(self, other):
        return self.title == other.title or self.author == other.author # Or book 1 and 2 has same author (True)

    def __lt__(self, other):
        return self.num_pages < other.num_pages

    def __gt__(self, other):
        return self.num_pages > other.num_pages

    def __add__(self, other):
        return f"{self.num_pages + other.num_pages} pages"

    def __contains__(self, keyword):
        return keyword in self.title or keyword in self.author

    def __getitem__(self, key):
        if key == "title":
            return self.title
        elif key == "author":
            return self.author
        elif key == "num_pages":
            return self.num_pages
        else:
            return f"Key {key} was not found"
book1 = Book("Noli Me Tangere", "Jose Rizal", 405)
book2 = Book("El Filibusterismo", "Jose Rizal", 354)
book3 = Book("Life and Writings of Rizal", "José P. Santos", 449)

# __str__ (STRING)
print(book1)
# print(book2)
# print(book3)

# __eq__ (EQUAL)
print(book1 == book2)

# __lt__ (LESS THAN)
print(book2 < book3)

# __gt__ (GREATER THAN)
print(book2 > book3)

# __add__ (ADD)
print(book1 + book3)

# __ contains__ (Contains - if the keyword in object title or author)
print("Noli Me Tangere" in book1)
print("Jose Rizal" in book1)
print("El Filibusterismo" in book2)
print("Jose Rizal" in book2)
print("Life and Writings of Rizal" in book3)
print("Jose Rizal" in book3)

# __getitem__
print(book1['title'])
print(book1['author'])
print(book1['num_pages'])

print(book2['title'])
print(book2['author'])
print(book2['num_pages'])

print(book3['title'])
print(book3['author'])
print(book3['num_pages'])









