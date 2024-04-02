def divide(a, b):
    return a/b

def main():
    try:
        # error (or exception) 발생가능한 구문
        a_str = input('a=')
        b_str = input('b=')
        
        r = divide(float(a_str),float(b_str))  #flout 으로 바꾸자.
        print(f'{r=}')
    
    except ValueError as ve:
        print(ve)
        raise ve 
    
    except ZeroDivisionError as zde:
        print(zde)
        
    except Exception as e:
        print(e)
        raise e
    except:
        print('------------')
        raise
    else:
        print('ok')
        
    finally:
        print('done')
        
if __name__ == "__main__":
    main()
