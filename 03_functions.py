def add(a: float, b: float) -> float:
    print(f'Adding {a} + {b}')
    return a + b

print(add(10,15))
print(add(15,40))

def greet(name: str, greeting: str = 'Hi') -> None:
    print(f'{greeting},{name}!')


greet('Rick','Ew')
greet('Ashmi','Hi')