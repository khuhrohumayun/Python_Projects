import random 


def rock_papar_scissor():
    choices =  ['rock', 'papar', 'scissors']

    user_choice = input('Enter your choice (rock, papar, scissors)'.lower())
    computer_choice = random.choice(choices)


    print(f'\nYou chose: {user_choice}')
    print(f'Computer chose: {computer_choice}')


    if user_choice == computer_choice:
        print("It's a tie!")

    elif(user_choice == 'rock' and computer_choice == 'scissors') or \
        (user_choice == 'scissors'  and computer_choice == 'papar') or \
        (user_choice == 'papar' and computer_choice == 'rock'):
        print("You win!")

    else:
        print("Computer wins!")



rock_papar_scissor()