import turtle


print("Suki is an Asian student - a new immigrant with limited English")
background = turtle.Screen()
#Images can be used with the turtle module.
# this assures that the size of the screen will always be 400x400 ..
background.setup(640, 423)

# set the screen background
background.bgpic("muahaha.jpg")

# Or, set the shape of a turtle00000
#screen.addshape("filename.png")
#tina = turtle.Turtle()
#tina.shape("filename.png")

Mark = turtle.Turtle()
Mark.shape("turtle")
Boy1 = turtle.Turtle()
Boy1.shape("mr. who.jpg")
#Boy1.color("green")
Girl1 = turtle.Turtle()
Girl1.shape("circle")
Suki = turtle.Turtle()

Suki.shape("triangle")

Mark.penup()
Mark.goto(-320,100)
Boy1.penup()
Boy1.goto(100,100)
Girl1.penup()
Girl1.goto(50,0)
GirlVoice = turtle.Turtle()
GirlVoice.shape("circle")
GirlVoice.color("red")
GirlVoice.hideturtle()
Suki.penup()
Suki.goto(-50,50)

GirlVoice.penup()
GirlVoice.goto(90,0)
GirlVoice.write("Oh, this is Suki, ")
GirlVoice.goto(90,-10)
GirlVoice.write("she's new to school.")
Boy1.write("Oh look an asian ching-chong!")

print("You are Mark, what do you do?")
print("A: Join in laughter")
print("B: Defend Suki")

Level1_Choice = input()
print Level1_Choice
if Level1_Choice == "A" or "a":
  Mark.write("Ha ha ha ha ha")

if Level1_Choice == "B":
  Mark.write("You guys, that's not nice. I'm Mark by the way.")

elif input != "A" :
  print ("Error")

elif input != "B" :
  print ("Error")

