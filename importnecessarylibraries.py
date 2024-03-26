# import necessary libraries
import math # to get pi



# define function
def get_circle_area(r): # function header
    # body of function
    area = math.pi * r **2
    return area # end of function body. return_value 반환. 디버깅 할 때 도움이 됨. 끊어치기임.

# return function
a = get_circle_area(3) # argument로 3을 취해주고 아래에 프린트 a로 실행.
print(a)
