from subpackage.module_b import greet_from_b
import os

if __name__ == "__main__":
    print(os.getcwd())
    print(f'{ os.path.dirname(__file__) = }')
    print(f'this is [{__name__}].')
    print(greet_from_b())
    