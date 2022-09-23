 
 


guess = 0

while True:
    number =  int(input("Enter the number that you guessed: "))
    if number != 50:
        print("wrong number")
        if number < 50:
            print("higher")
        else:
            print("lower")
        
        guess += 1
    elif number == 50:
        print("Correct!")
        print(f"you have {guess} total guesses.")
        break

