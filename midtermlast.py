import random #imports the random function
part1 = True #starts part 1
addpoint = 1 #creats addpoint global variable

g = open("paulread.txt", "a")
g.write("Hello World")
g.close()

g = open("paulread.txt", "r")
print(g.read())

import math
print("You have: ", math.pi, "credits")

class Casino: #creates a class called casino
  def __init__(self, city, country): #defines the class
    self.city = city #defines city
    self.country = country #defines country
  def introduce_self (self): #defines the function introduce_self
    print ("Casino is located in: " + self.city) #prints
    print ("Which is in the country of: " + self.country)
c1 = Casino ("Las Vegas", "USA") 
c2 = Casino ("London", "England")
c1.introduce_self()

while part1: #tells what happens in part 1
  introlist = ["Welcome to Dice Roll! Type start to begin! ", "to Dice Roll!", "Type start to begin!"] #creates a list
  print(introlist[-3]) #prints the member 3rd from the end
  if input() == "start": #if the input = start, it will print the text bellow
    print('Please enter the name you would like to use below!')
    playername = input() #defines the variable playername as the input
    part1 = False #stopping part 1
    part2 = True #starting part 2
  else:
    print("Before you go, watch me infinitley add up the sides of the dice!") #prints
    sum = 0
    sides = 1
    while sides < 7:
      sum = sum + sides
      print("Numbers of sides: " + str(sides) + " Dots on sides: " + str(sum))
    part1 = False #stopping at part 1 - will not repeat

while part2: #starts part 2
  def cheer_function(): #defining the cheer function
    print("You'll get it next time.") #what the cheer function does

  def give_point(): #defining the give point function
    print("You get an extra point! Wooooo!!!")

  playernumber = random.randint(1,6) #chooses a random integer 1-6 and assigns it to playernumber
  botnumber = random.randint(1,6) #chooses a random integer 1-6 and assigns it to the bot
  if botnumber > playernumber: #compares the two numbers
    print("Uh Oh... Computer wins with a score of: " + str(botnumber)) #prints the computer wins with the integer variable
    cheer_function()
    part2 = False #ends part
  else:
    print("Yay! " + str(playername) + " wins with a score of:" + str(playernumber))
    give_point()
    part2 = False

