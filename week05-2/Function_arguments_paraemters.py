def test_func(*pack):
    print(type(pack),pack)
    for idx, c in enumerate(pack):
        print(f'{idx:02} : {str(c):>14}')
        
test_func('사과','바나나','복숭아','자두')