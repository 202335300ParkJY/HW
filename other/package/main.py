from test import calculate_atan, atan_in_degrees

def main():
    number = 1
    radian_result = calculate_atan(number)
    degree_result = atan_in_degrees(number)
    print(f"{number}의 아크탄젠트(라디안 단위)는: {radian_result}")
    print(f"{number}의 아크탄젠트(도 단위)는: {degree_result}")

if __name__ == "__main__":
    main()
