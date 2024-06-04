#!/bin/env python

#juy_run.py 파일 : main script file

#import juy_cal
from juy_cal import juy_addition

import sys

if "juy_cal" is sys.modules:
    print("1: ok!")
    
sys.path.append("D:\\xxx_yyy")

from juy_cal import juy_addition

if "juy_cal" is sys.modules:
    print("1: ok!")
print('=================================\n\n')

print(f'{sys.path = }')
print('=================================\n\n')

def main():
    while True:
        try:
            a_str = input('Enter the first operand:')
            a = float(a_str)
            b_str = input('Enter the second operand:')
            b = float(b_str)
            
            #r = juy_cal.juy_addition(a, b)
            r = juy_addition(a, b)
            
            print(f'result = {r}')
            break
        except ValueError as ve:
            print('[ValueError] Invaild Input! Try again!')
            
if __name__ == '__main__':
    print(f'{__file__}')
    main()
    