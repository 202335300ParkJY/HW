#!/bin/env python

# ds_run03.py
import farith.juy_cal as fundamental
import ftri.juy_cal as tri

def main():

    while True:
        try:
            a_str = input('Enter the first operand:')
            a = float(a_str)
            b_str = input('Enter the second operand:')
            b = float(b_str)

            print(f'{a}+{b}={fundamental.ds_addition(a,b)}')

            rad = float(input('Enter the radian to get the value of cosine:'))
            print(f'cos of {rad}={tri.ds_cos(rad)}')
            break
        except ValueError as ve:
            print(ve)

if __name__ == '__main__':
    main()

            