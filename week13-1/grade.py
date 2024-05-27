#from random import choice
import random

def get_grade():
    
    print(f'{__name__=}')
    
    grades = ['A+','A0','B+','B0','C+','C0','D+','D0','F']
    #return choice(grades)
    return random.choice(grades)