score=[120,100,80,60,40,20,0]
games_played=0
high_score=0
import os
import json
from operator import itemgetter

class guess_number:

    def write_scores(self,player_name,score,games):
        players = {"name":player_name,"score": score,"games": games}
        with open('scores.json','a+') as file:
            json.dump(players,file) #insert data
            file.write('\n') #insert line
            file.close()
 
    def game(self,player):
        global games_played
        global score
        global high_score
        games_played+=1
        import random
        number=random.randint(1,20)
        turns=6
        num_guesses=0
        guess_correct=False
        inserted_numbers_list=[]
        while turns>0:
            while True:
                try:
                    print('Take a guess')
                    guess = int(input()) 
                    break
                except ValueError:
                    print("Oops!  That was no valid number.  Try again...")
            turns-=1
            if inserted_numbers_list.count(guess) >0:
                print('You already inserted '+str(guess)+',try again')
                turns+=1
            else:
                inserted_numbers_list.append(guess)
                if guess>number:
                    num_guesses+=1
                    print('Your guess is too high.')
                elif guess<number:
                    num_guesses+=1
                    print('Your guess is too low.')
                else:
                    num_guesses+=1
                    print('Good job, ' +player + '! You guessed my number in ' + str(num_guesses) + ' guesses!')
                    high_score=high_score+score[num_guesses-1]
                    guess_correct = True
                    break
        if guess_correct==False:
            print('Sorry. The number I was thinking of was ' + str(number))
            high_score=high_score+score[num_guesses]
    def __init__(self):
        super().__init__()
        answer = None
        playerName=input('Hello!What is your name? \n')
        print('Well, ' + playerName + ', I am thinking of a number between 1 and 20.You have 6 tries,good luck.')
        self.game(playerName)
        while answer not in ('Y', 'N'):
            answer = input('Do u want to play again Y/N ')
            if answer.upper() == 'Y':
                self.game(playerName)
            elif answer.upper() == 'N':
                answer='N'
                self.write_scores(playerName,high_score,games_played)
            else:
                print('Please enter Y or N.')

x=guess_number()
input('Press ENTER to exit')
