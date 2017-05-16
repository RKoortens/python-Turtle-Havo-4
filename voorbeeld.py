import turtle

sp = turtle.Turtle()

# definitie basisvormen
def tekenrechthoek(x, y, lengte, breedte, vulkleur, penkleur):
    # instellingen van de schildpad
    sp.penup()
    sp.pencolor(penkleur) # kleur van de omtreklijn
    sp.setheading(0)
    sp.begin_fill()
    sp.fillcolor(vulkleur) # kleur van de vulling
    sp.goto(x,y)
    sp.pendown()
    # tekenen
    for teller in (1, 2):
        sp.forward(lengte)
        sp.left(90)
        sp.forward(breedte)
        sp.left(90)
    sp.end_fill()
    # klaar met tekenen


def tekenvierkant(x, y, lengte, vulkleur, penkleur):
    sp.penup()
    sp.pencolor(penkleur)
    sp.setheading(0)
    sp.begin_fill()
    sp.fillcolor(vulkleur)
    sp.goto(x,y)
    sp.pendown()
    for teller in (1, 2, 3, 4):
        sp.forward(lengte)
        sp.left(90)
    sp.end_fill()


def tekendriehoek(x, y, lengte, vulkleur, penkleur):
    sp.penup()
    sp.pencolor(penkleur)
    sp.setheading(0)
    sp.begin_fill()
    sp.fillcolor(vulkleur)
    sp.goto(x,y)
    sp.pendown()
    for teller in (1, 2, 3):
        sp.forward(lengte)
        sp.left(120)
    sp.end_fill()
 

def tekencirkel(x, y, straal, vulkleur, penkleur):
    sp.penup()
    sp.setheading(0)
    sp.pencolor(penkleur)
    sp.begin_fill()
    sp.fillcolor(vulkleur)
    sp.goto(x,y)
    sp.pendown()
    sp.circle(straal)
    sp.end_fill()
    

def tekenhuis1():
    tekenrechthoek(0, 0, 200, 200, "brown", "black")
    tekendriehoek(0, 200 , 200, "brown", "black")
    tekenvierkant(15, 50, 75, "Light Steel Blue", "black")
    tekenrechthoek(100, 0, 80, 125, "Dark Olive Green", "black")
    tekencirkel(120, 60, 7, "red", "black")

def tekenstraat(x, y, lengte, breedte, vulkleur, penkleur):
    tekenrechthoek(x, y, lengte, breedte, vulkleur, penkleur)

def tekenstoep(x, y, lengte, breedte, vulkleur, penkleur):
    tekenrechthoek(x, y, lengte, breedte, vulkleur, penkleur)

def tekengras(x, y, lengte, breedte, vulkleur, penkleur):
    tekenrechthoek(x, y, lengte, breedte, vulkleur, penkleur)

def tekenlucht(x, y, lengte, breedte, vulkleur, penkleur):
    tekenrechthoek(x, y, lengte, breedte, vulkleur, penkleur)
    
def maaktekening():
    sp.penup()
    tekenlucht(-400, 100, 800, 400, "blue", "blue")
    tekengras(-400, 0, 800, 100, "green", "green")
    tekengras(-400, -400, 800, 200, "green", "green") 
    tekenstraat( -400, -200, 800, 200, "black", "black")
    tekenstoep( -400, -200, 800, 45, "grey", "black")
    tekenstoep( -400, -45, 800, 45, "grey", "black")
    tekenhuis1()
    sp.hideturtle()

maaktekening()
