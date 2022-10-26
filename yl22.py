import random

while True:
    user_action = input("Vali (kivi, paber, käärid): ")
    possible_actions = ["kivi", "paber", "käärid"]
    computer_action = random.choice(possible_actions)
    print(f"\nSa valisid: {user_action}, arvuti valis {computer_action}.\n")

    if user_action == computer_action:
        print(f"Mõlemad mängijad valisid {user_action}. See on viik!")
    elif user_action == "kivi":
        if computer_action == "käärid":
            print("kivi tapab käärid! Sa võidad!")
        else:
            print("paber tapab kivi! Sa kaotad.")
    elif user_action == "paber":
        if computer_action == "kivi":
            print("paber tapab kivi! Sa võidad!")
        else:
            print("käärid tapab paberi! Sa kaotad.")
    elif user_action == "käärid":
        if computer_action == "paber":
            print("käärid tapab paberi! Sa võidad!")
        else:
            print("kivi tapab käärid! Sa kaotad.")

    play_again = input("Tahad veel mängida? (j/e): ")
    if play_again.lower() != "j":
        break
