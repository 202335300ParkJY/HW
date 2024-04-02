for i, c in enumerate(range(2,5)):
    print(f'{i=}')
    if i % 2 == 1:
        continue
    print(f'{i},{c}')