#!/usr/bin/env python3

# The signatures of this class and its public methods are required for the automated grading to work. 
# You must not change the names or the list of parameters.
# You may introduce private/protected utility methods though.
class Publication:

    def __init__(self, authors, title, year):
        self.__authors = authors
        self.__title = title
        self.__year = year
    
    def __repr__(self) -> str:
        representation = f"Publication({str(self.__authors)}, \"{self.__title}\", {self.__year})"
        return representation.replace("'", "\"")

    def __str__(self) -> str:
        representation = f"Publication({str(self.__authors)}, \"{self.__title}\", {self.__year})"
        return representation.replace("'", "\"")

    def __hash__(self) -> int:
        return hash((tuple(self.__authors), self.__title, self.__year))


    #Comparison "=="
    def __eq__(self, other: object) -> bool:
        #Check if the other object is of same Type
        if isinstance(other, Publication):
            return self.__authors == other.get_authors() and self.__title == other.get_title() and self.__year == other.get_year()
        return NotImplemented

    #Comparison "!="
    def __ne__(self, other):
        if isinstance(other, Publication):
            return self.__authors != other.get_authors() or self.__title != other.get_title() or self.__year != other.get_year()
        return NotImplemented

    #Comparison "<"
    #Vergleich umgekehrt --> Unnötoge Linien vermeiden
    def __lt__(self, other):
        if not isinstance(other, Publication):
            return NotImplemented
        if sorted(self.__authors) != sorted(other.get_authors()):
            return sorted(self.__authors) < sorted(other.__authors)
        if self.__title != other.get_title():
            return self.__title < other.get_title()
        if self.__year != other.get_year():
            return self.__year < other.get_year()


    #Compariosn ">"
    def __gt__(self, other):
        if not isinstance(other, Publication):
            return NotImplemented
        if sorted(self.__authors) != sorted(other.get_authors()):
            return sorted(self.__authors) > sorted(other.__authors)
        if self.__title != other.get_title():
            return self.__title > other.get_title()
        if self.__year != other.get_year():
            return self.__year > other.get_year()

    #Operator "<="
    def __le__(self, other):
        return self.__lt__(other) or self.__eq__(other)

    #Operator ">="
    def __ge__(self, other):
        if not isinstance(other, Publication):
            return NotImplemented
        return self.__gt__(other) or self.__eq__(other)

    def get_authors(self):
        copy = []
        for el in self.__authors:
            copy.append(el)
        return copy
    
    def get_title(self):
        return self.__title

    def get_year(self):
        return self.__year

    # To implement the required functionality, you will also have to implement several
    # of the special functions that typically include a double underscore.


# You can play around with your implementation in the body of the following 'if'.
# The contained statements will be ignored while evaluating your solution.
if __name__ == '__main__':
    references = [
        Publication(["Gamma", "Helm", "Johnson", "Vlissides"], "Design Patterns", 1994),
        Publication(["Cockburn"], "Writing Effective Use Cases", 2000),
        Publication(["Duvall", "Matyas", "Glover"], "Continuous Integration", 2007)
    ]

    p = Publication(["Duvall", "Matyas", "Glover"], "Continuous Integration", 2007)
    s = "Publication([\"Duvall\", \"Matyas\", \"Glover\"], \"Continuous Integration\", 2007)"
    print(p)
    print(s)
    print(str(p) == s)

    p1 = Publication(["A"], "B", 1234)
    p2 = Publication(["A"], "B", 1234)
    p3 = Publication(["B"], "C", 2345)
    p4 = Publication(["A"], "A", 1324)

    print(p1 == p2)  # True
    print(p2 == p3)  # False

    sales = {
        p1: 273,
        p3: 398,
    }

    print(p != p3)
