#Job9

def type_triangle(a, b, c):
    if a + b > c and a + c > b and b + c > a:
        if a == b == c:
            print("Triangle équilatéral")
        elif a == b or a == c or b == c:
            if a**2 + b**2 == c**2 or a**2 + c**2 == b**2 or b**2 + c**2 == a**2:
                print("Triangle rectangle isocèle")
            else:
                print("Triangle isocèle")
        elif a**2 + b**2 == c**2 or a**2 + c**2 == b**2 or b**2 + c**2 == a**2:
            print("Triangle rectangle")
        else:
            print("Triangle quelconque")
    else:
        print("Ces longueurs ne peuvent pas former un triangle")

a = 7       
b = 8   
c = 6
type_triangle(a, b, c)