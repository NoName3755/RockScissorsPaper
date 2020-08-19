def game():    
    Nog = 1
    poc = 0
    poh = 0
    print("\t\t\t\t Rock Scissor Paper")
    print("'R' for 'Rock' \n'S' for 'Scissor' \n'P' for 'Paper'\n")
    print("If you enter wrong then your trun will be dismissed")
    while Nog <= 10:
        import random
        lst = ["R", "S", "P"]
        sign_c = random.choice(lst)
        print("Enter Here")
        sign = input()
        sign_h = sign.upper()

        if sign_c == sign_h:
            print("Tie \nNo one wil get points")

        elif sign_c == 'R' and sign_h == 'S':
            poc = poc + 1
            print("You Lose")

        elif sign_c == 'R' and sign_h == 'P':
            poh = poh + 1
            print("You Win")

        elif sign_c == 'S' and sign_h == 'R':
            poh = poh + 1
            print("You Win")

        elif sign_c == 'S' and sign_h == 'P':
            poc = poc + 1
            print("You Lose")

        elif sign_c == 'P' and sign_h == 'R':
            poc = poc + 1
            print("You Lose")

        elif sign_c == 'P' and sign_h == 'S':
            poh = poh + 1
            print("You win")

        else:
            print("Invalid input")
        print(f"\nYou entered '{sign_h}'\nComputer entered '{sign_c}'")
        print("\n", 10 - Nog, "turn left\n")
        Nog = Nog + 1
    print("Result of 10 times:\n\n"
          "Your total point is", poh, "\nComputer total point is", poc)
    if poh < poc:
        print("\nYou Lose")
    elif poh > poc:
        print("\nYou Win")
    else:
        print("\nTie")
    again()


def again():
    repeat = input("Do you want to continue y/n\n")
    ree = repeat.lower()
    if ree == 'y':
        game()
    elif ree == 'n':
        print("See you later")
    else:
        again()


game()
