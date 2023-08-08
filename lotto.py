#-----Lotto simulator-----
#Lassi Helin


#User selects 7 numberes from 1-41
#All numbers must be unique

#Simulator selects 7 numberes from 1-41
#All numbers must be unique

#Finally the program prints how many guessed numbers were correct
#And if all are correct, the user wins


import random

inputlist = []
print("Give 7 numbers in the range of 1-41")
inputlaskuri = 0


while inputlaskuri < 7:
    userinput = input()
    if int(userinput) not in inputlist:
        inputlist.append(int(userinput))
        inputlaskuri += 1
    else:
        print("You have already given this number!")
        continue
    
lotterylist = []
randomlaskuri = 0

while randomlaskuri < 7:
    randomint = random.randint(1,41)
    if int(randomint) not in lotterylist:
        lotterylist.append(int(randomint))
        randomlaskuri += 1
    else:
        continue

vertauslaskuri = 0
listalaskuri = 0
points = 0

while vertauslaskuri < 7:
    if inputlist[listalaskuri] in lotterylist:
        points += 1
        vertauslaskuri += 1
        listalaskuri += 1
    else:
        vertauslaskuri += 1
        listalaskuri += 1
        continue

if points == 7:
    print("You got 7 points, you won!")
else:
    print("You got " + str(points) + " points!")