# Class which contain methods to calculate area of some shapes.

class Basic_Operations:
    def self_arg(self):
        pass

    def ar_of_tri(self):
        b = input("Enter the value of base of a triagle: ")
        base = float(b)
        h = input("Enter the value of height of a triangle: ")
        height = float(h)
        Area_of_Triangle = 1/2 * base * height
        print('Required Area of triangle = ',Area_of_Triangle)
    
    def ar_of_sq(self):
        s = input("Enter the value of side of a Square: ")
        side = float(s)
        Area_of_sq = side * side
        print("Required Area of square = ",Area_of_sq)

    def ar_of_cir(self):
        r = input("Enter the value of radius of a circle: ")
        radius = float(r)
        Area_of_circle = 3.14 * radius * radius
        print("Required Area of circle = ",Area_of_circle)

    def ar_of_rect(self):
        l = input("Enter the value of length of a Rectangle: ")
        length = float(l)
        w = input("Enter the value of weight of a Rectangle: ")
        weight = float(w)
        Area_of_Rectangle = weight * length
        print('Required Area of Rectangle = ',Area_of_Rectangle)

# You can add more operations or methods in above Basic_Operations class.
        
AreaOfTriangle = Basic_Operations()
AreaOfSquare = Basic_Operations()
AreaOfCircle = Basic_Operations()

# You Must need to call method in order to get required output. Call the method below this comment.
AreaOfTriangle.ar_of_tri()

# www.instagram.com/gokulsuthar22
