import random
import os

def fortuneAnswer(number):
    if number == 1:
        return 'Yes'
    if number == 2:
        return 'No'
    if number == 3:
        return 'Reply uncertain, please ask again..'
    if number == 4:
        return 'Ask again later'
    if number == 5:
        return 'Outlook not so good'
    if number == 6:
        return 'Very doubtful'
    if number == 7:
        return 'It is decidedly so'
    if number == 8:
        return 'It is certain'

fortune = fortuneAnswer(random.randint(1,8))
os.system('cls')
print(fortune)