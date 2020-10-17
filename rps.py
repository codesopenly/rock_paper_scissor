# Write your code here
import random
game = {'rock' :'paper' , 'paper':'scissors', 'scissors':'rock'}
name = input('Enter your name: ')
print(f'Hello, {name}')
initial = 0
dict ={}
dict[name] = initial
f = open("rating.txt","w")
f.write( str(dict) )
f.close()
while True:
    user_input = input()
    if user_input in ['rock', 'paper', 'scissors', '!exit','!rating']:
        if user_input != '!rating':
            if user_input != '!exit':
                listq = ['rock','paper','scissors']
                computer_choce = random.choice(listq)
                if user_input == computer_choce:
                    print(f'There is a draw ({user_input})')
                    dict[name] += 50
                elif game[user_input] == computer_choce:
                    print(f'Sorry, but computer chose {computer_choce}')
                else:
                    print(f'Well done. Computer chose {computer_choce} and failed')
                    dict[name] += 100
            else:
                print('Bye!')
                break
        else:
            print(f'Your rating: {dict[name]}')
    else:
        print('Invalid input')
