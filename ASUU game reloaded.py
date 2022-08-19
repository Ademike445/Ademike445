



name = input("Type your name: ").title()
print(f"Welcome to ASUU GAME , {name:}!")


answer = input("Do you want to attend higher institution in Nigeria? (Yes/No) ").lower().strip()

if answer == "yes":
    while True:
        answer = input(" Which among these do you plan to attend: COE, POLY or UNI: ").lower().strip()
        if answer == "coe":
            print("That's a great choice, you have escaped ASUU, bye!\nThank you for playing ASUU game")
            quit()
            
        elif answer == "poly":
            print("Good! You actually escaped ASUU but there is still ASUP, bye!\nThank you for playing ASUU game")
            quit()
            
        elif answer == "uni":
            print("Welcome to the University System!")
            break
        else:
            print("Invalid Respond!")
                    
    answer = input("Did you pass WAEC and JAMB? (Yes/No)? ").lower().strip()

    if answer == "no":
        print("Oops! you have to pass WAEC and JAMB to continue, Bye!")
    elif answer == "yes":
        while True:
            try:
                answer = int(input("How many year is your course of study? Type the numbers of year "))
                break
            except ValueError:
                print("Type a number!")

        print ("The ASUU year for this course is:", (str(answer+3))+ "yrs")
        answer = input("Do you agree with ASUU? (Yes/No)? ").lower().strip()
        if answer == "no":
            print("JAPA, JAPA, JAPA, Bye!")
        else:
            print(f'Congratulation! {name} \nWelcome to the struggle.')
            
            


else:
    print(f'Awesome {name} enjoy your studies abroad, bye!')

print("Thank you for playing ASUU game")
    
