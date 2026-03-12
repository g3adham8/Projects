import random
while True:

    choice = ("r", "p", "s")
    emojes = {'r': '🪨', 's': '✂️', 'p': ' 📜'}

    my_choice = input("Rock , Paper or Scissor? (r\\p\\s) ").lower().strip()

    if my_choice not in choice:
        print("Invalid choice")
        continue    # ====> عشان ترجع تاني من الاول وميحصلش ايرور
    computer_choice = random.choice(choice)

    print(f"you chose {emojes[my_choice]}")
    print(f"computer chose {emojes[computer_choice]}")

    if my_choice == computer_choice:
        print("Draw")
    elif (
        (my_choice == 'r' and computer_choice == 's') or
        (my_choice == 's' and computer_choice == 'p') or
            (my_choice == 'p' and computer_choice == 'r')):
        print("you win")
    else:
        print("you lose")

        x = input("Do you want to continue? (y\\n)").lower().strip()
        if x == 'n':
            break
        else:
            continue
