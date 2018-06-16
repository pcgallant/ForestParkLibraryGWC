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
boy1 = turtle.Turtle()

background.addshape("sneakers.jpg")
background.addshape("converse lady 200.gif")

boy1.shape("sneakers.jpg")
#boy1.shape("mr. who.jpg")
boy1.color("green")
Girl1 = turtle.Turtle()
Girl1.shape("converse lady 200.gif")
Suki = turtle.Turtle()

background.addshape("boom chicka chicka3.jpg")
Boy2 = turtle.Turtle()
Boy2.shape("boom chicka chicka3.jpg")
Boy2.right(269)
Suki.shape("triangle")

Mark.penup()
Mark.goto(-320,100)
boy1.penup()
boy1.goto(30,-100)
Girl1.penup()
Girl1.goto(100,-100)
GirlVoice = turtle.Turtle()
GirlVoice.shape("circle")
GirlVoice.color("red")
GirlVoice.hideturtle()
Suki.penup()
Suki.goto(-50,50)
Boy2.goto(5,-100)

GirlVoice.penup()
GirlVoice.goto(90,0)
GirlVoice.write("Oh, this is Suki, ")
GirlVoice.goto(90,-10)
GirlVoice.write("she's new to school.")
boy1.write("Oh look an asian ching-chong!")

print("You are Mark, what do you do?")
print("A: Join in laughter")
print("B: Defend Suki")

Level1_Choice = input()
print Level1_Choice
if Level1_Choice == "A":
  Mark.write("Ha ha ha ha ha")

if Level1_Choice == "B":
  Mark.write("You guys, that's not nice. I'm Mark by the way.")

elif input != "A" :
  print ("Error")

elif input != "B" :
  print ("Error")
  


