import turtle

casper = turtle.Turtle()
listOfColors = ["red","green","blue","yellow"]

for c in listOfColors:
   print(c)

for i in range(4):
  print(i)

# range(4) is internally this list [0,1,2,3]

# Accessing list elements
# If you don't remember, use documentation (e.g. w3schools [search python lists])

# Accessing third element of listOfColors
print(listOfColors[2])

# String concantenation
print("The third element of listOfColors is: " + listOfColors[2])

# Assigning a variable to the store the third element
v = listOfColors[2]
print ("The value of variable v is: " + v)

def redSquare(turtleName,sideLength):
  turtleName.color("red")
  for i in range(4):
    turtleName.color("red")
    turtleName.forward(sideLength)
    turtleName.left(90)

def blueTriangle(turtleName,sideLength):
  turtleName.color("blue")
  for i in range(3):
    turtleName.forward(sideLength)
    turtleName.left(120)

redSquare(casper, 50)
blueTriangle(casper, 30)