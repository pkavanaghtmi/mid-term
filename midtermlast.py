import random #imports the random function
part1 = True #starts part 1
addpoint = 1 #creats addpoint global variable

class Casino:
  def __init__(self, city, country):
    self.city = city
    self.country = country
  def introduce_self (self):
    print ("Casino is in " + self.city)
    print ("Which is in the country of " + self.country)
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
    print("Before you go, watch me add up the sides of the dice!") #prints
    sum = 0
    sides = 1
    while sides<7:
        sum = sum + sides
        print("Numbers of sides: " + sides + " Dots on sides: " + sum)
    part1 = False #stopping at part 1 - will not repeat

while part2: #starts part 2
  def give_point(): #defining the give point function
    playernumber +- addpoint #eaquivalent to playernumber = addpoint + playernumber
    print("You got a free point and your new score is" + str(playernumber))

  playernumber = random.randint(1,6) #chooses a random integer 1-6 and assigns it to playernumber
  botnumber = random.randint(1,6) #chooses a random integer 1-6 and assigns it to the bot
  if botnumber > playernumber: #compares the two numbers
    print("Uh Oh... Computer wins with a score of: " + str(botnumber)) #prints the computer wins with the integer variable
    part2 = False #ends part
    part3 = True #begins part 3
  else:
    print("Yay! " + str(playername) + " wins with a score of:" + str(playernumber))
    part2 = False  #ends part 2
    part3 = True #begins part 3

while part3:
  print("Time for a bonus! Type +1 to recieve a free point!")
  if input() == +1:
    give_point()

  def cheer_function(): #defining the cheer function
    print("Wow! You are doing great!") #what the cheer function does

  while playernumber < 2: #gives perameters to the funtion
    cheer_function()#initiates the cheer function
