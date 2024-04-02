def divide(a, b):
    return a/b

def main():
    try:
        # error (or exception) 발생가능한 구문
        a_str = input('numerator=?')
        a = int(a_str)
        
        b_str = input('numerator=?')
        b = int(b_str)
        
        r = divide(a,b)
        print(f'result = {r}')
    except ValueError as ve:
        print(ve)
        print(f'Check your inputs')
        raise ValueError("잘못된 input value입니다.")
    
    except ZeroDivisionError as ve:
        print(ve)
        print(f'denominator can not be zero!')
        
    finally:
        print('This python script is finished.')
        
main()
