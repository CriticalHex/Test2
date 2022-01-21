#Write a program that asks a player to enter their score. If the score is over 9,000, tell them they're amazing. 
#If it's under 100, tell them to "get gud". Tell them to keep practicing for any other score. 

#Write a for loop that prints out the numbers from 10-100 counting by 5s.

#Write a while loop that prints out "CHEESE" 12 times. 

#Write class cheese. Class cheese has an x and y position and another variable isMelted. It has functions to melt, and printInfo. 

#Instantiate 2-3 cheeses and print their information. Then melt the cheese and reprint the information. 

class Cheese():
    def __init__(self,position):
        self.position = position
        self.isMelted = False
    def printInfo(self):
        print("Melted:", self.isMelted, " Position:", self.position)
    def melt(self):
        self.isMelted = True

user_input = int(input("Enter your score: "))

if user_input > 9000:
    print("Wow! You're amazing!")
elif user_input < 100:
    print("Yikes, git gud bro.")
else:
    print("Eh... keep practicing.")

print()

for i in range(10,105,5):
    print(i)

print()

sayCheese = 0

while sayCheese < 12:
    print("CHEESE")
    sayCheese += 1

print()

cheese1 = Cheese((100,200))
cheese2 = Cheese((700,300))
cheese3 = Cheese((400,900))

cheese1.printInfo()
cheese2.printInfo()
cheese3.printInfo()

cheese1.melt()
cheese2.melt()
cheese3.melt()

print()

cheese1.printInfo()
cheese2.printInfo()
cheese3.printInfo()
