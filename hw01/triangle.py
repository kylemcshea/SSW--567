#Kyle McShea
#SYS 581
#I pledge my honor that I have abided by the Stevens Honor System
#10422944

#Homework 1

def classify_triangle(a,b,c):
    if type(a) == int and type(b) == int and type(c) == int:
        if(a == b == c):
            return "equilateral"
        elif(a == b or b == c or a == c):
            return "isosceles"
        elif(a ** 2 + b ** 2 == c ** 2):
            return "right"
        elif(a != b and a != c and b != c):
            return "scalene"
    else:
        return "Integer Input only"
