if __name__ == '__main__':
    # main script로
    print(f'main script mode :{__name__}')
else:
    # module로 import 인 경우 수행.
    print(f"this is echo's init part : {__name__}")