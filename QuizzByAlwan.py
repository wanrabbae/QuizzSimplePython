score = 0

# Soal 1
soal1 = input("What color is the Apple? \n a. Red \n b. Yellow \n c. Pink \nAnswer: ")
if soal1 == "a":
    print("You are correct!")
    score += 10
    print("Score: ",score)
    print("\n")
else:
    print("You are incorrect!")
    print("Score: ",score)
    print("\n")

# Soal 2
soal2 = input("What color is the Banana? \n a. Pink \n b. Yellow \n c. Blue \nAnswer: ")
if soal2 == "b":
    print("You are correct!")
    score += 10
    print("Score: ",score)
    print("\n")
else:
    print("You are incorrect!")
    print("Score: ",score)
    print("\n")

# Soal 3
soal3 = input("What color is the Grape? \n a. Purpple \n b. Blue \n c. Pink \nAnswer: ")
if soal3 == "a":
    print("You are correct!")
    score += 10
    print("Score: ",score)
    print("\n")
else:
    print("You are incorrect!")
    print("Score: ",score)


#FINAL MESSAGE
if score <= 10:
    print("Score kamu: ",score,"You suck!")
elif score == 20:
    print("Score kamu: ",score,"You great!")
else:
    print("Score kamu: ",score,"You perfect!")
