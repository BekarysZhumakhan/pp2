#function_1
#1
def convert(grams):
    ounces = 28.3495231 * grams
    return ounces
grams=int(input("enter the number:"))
print(convert(grams))
#2
def temp(F):
    C = (5 / 9) * (F - 32)
    return C
F=int(input("enter temp:"))
print(temp(F))
#3
def solve(nh,nl):
    for y in range(nh+1):
        x=nh-y
        if y*2+x*4==nl:
            return x,y
        
    return "wrong"
nh=int(input("enter the number of heads:"))
nl=int(input("enter the number of legs:"))
print(solve(nh,nl))
#functions_2
movies = [
{
"name": "Usual Suspects", 
"imdb": 7.0,
"category": "Thriller"
},
{
"name": "Hitman",
"imdb": 6.3,
"category": "Action"
},
{
"name": "Dark Knight",
"imdb": 9.0,
"category": "Adventure"
},
{
"name": "The Help",
"imdb": 8.0,
"category": "Drama"
},
{
"name": "The Choice",
"imdb": 6.2,
"category": "Romance"
},
{
"name": "Colonia",
"imdb": 7.4,
"category": "Romance"
},
{
"name": "Love",
"imdb": 6.0,
"category": "Romance"
},
{
"name": "Bride Wars",
"imdb": 5.4,
"category": "Romance"
},
{
"name": "AlphaJet",
"imdb": 3.2,
"category": "War"
},
{
"name": "Ringing Crime",
"imdb": 4.0,
"category": "Crime"
},
{
"name": "Joking muck",
"imdb": 7.2,
"category": "Comedy"
},
{
"name": "What is the name",
"imdb": 9.2,
"category": "Suspense"
},
{
"name": "Detective",
"imdb": 7.0,
"category": "Suspense"
},
{
"name": "Exam",
"imdb": 4.2,
"category": "Thriller"
},
{
"name": "We Two",
"imdb": 7.2,
"category": "Romance"
}
]


def first(movies):
    a=input('MOVIE NAME: ')
    for films in movies:
        if films['name']==a and films['imdb']>5.5:
            return True
print(first(movies))
print()
#2
def second(movies):
    ar=[]
    for mov in movies:
        if mov['imdb']>5.5:
            ar.append(mov['name'])
    return ar
print(second(movies))
print()
#3
def third(movies):
    cat=input("CATEGORY: ")
    mydict={cat:[]}
    for film in movies:
        if film['category']==cat:
            mydict[cat].append(film['name'])
    return mydict
print(third(movies))
print()
#4
def fourth(movies):
    sum=0
    for mov in movies:
        sum+=mov['imdb']
    return sum/len(movies)
print(fourth(movies))
print()
#5
def fifth(movies):
    cat=input("CATEGORY: ")
    sum=0
    cnt=0
    for films in movies:
        if films['category']==cat:
            sum+=films['imdb']
            cnt+=1
    return sum/cnt
print(fifth(movies))
#Classes
#1
class exercise:
    def _init_(self):
        self.text = ""
    def getString(self):
        self.text = input("enter a string:")
    def printString(self):
        print(self.text.upper())
objects = exercise()
objects.getString()
objects.printString()
#2
class Shape:
    def _init_(self):
        pass  

    def area(self):
        return 0  

class Square(Shape):
    def _init_(self, length):
        self.length = length  

    def area(self):
        return self.length * self.length  
    
square = Square(5)  
print("Square area:", square.area()) 

shape = Shape()
print("Shape area:", shape.area())  
#3
class Shape:
    def _init_(self):
        pass  

    def area(self):
        return 0  

class Rectangle(Shape):
    def _init_(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width  
rectangle = Rectangle(5, 4)  
print("Rectangle area:", rectangle.area()) 
shape = Shape()
print("Shape area:", shape.area())  
#4
import math
class Point:
    def _init_(self, x, y):
        self.x = x 
        self.y = y  

    def show(self):
        print(f"Point coordinates: ({self.x}, {self.y})")  

    def move(self, dx, dy):
        self.x += dx  
        self.y += dy  
        print(f"Moved to: ({self.x}, {self.y})")  

    def dist(self, other_point):
        distance = math.sqrt((self.x - other_point.x)*2 + (self.y - other_point.y)*2)
        return distance
point1 = Point(1, 2)
point1.show() 
point2 = Point(4, 6)
point2.show()  
point1.move(2, 3)  
distance = point1.dist(point2)
print("Distance between points:", distance)
