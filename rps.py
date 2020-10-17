# Write your code here
import random
game = {'rock' :'paper' , 'paper':'scissors', 'scissors':'rock'}

while True:
    user_input = input()
    if user_input in ['rock', 'paper', 'scissors', '!exit']:
        if user_input != '!exit':
            listq = ['rock','paper','scissors']
            computer_choce = random.choice(listq)
            if user_input == computer_choce:
                print(f'There is a draw ({user_input})')
            elif game[user_input] == computer_choce:
                print(f'Sorry, but computer chose {computer_choce}')
            else:
                print(f'Well done. Computer chose {computer_choce} and failed')
        else:
            print('Bye!')
            break
    else:
        print('Invalid input')
