text = 'apple'
number =  10
decimal = -10.123
has_money = True
coordinates = (2.5, 1.5) #immutable
names = ['Agnetha', 'Bjorn', 'Benny', 'Blanco' ] #mutable
unique = {1,2,3,4,4,5} #no duplicates allowed
users = {'Bob':1, 'James':2, 'Marley':3}

#sometimes you might have to convert the numbers

number = '100'
print(10 + int(number))
print(10 + float(number))

#type annotations?

age: int = 10
name: str = 'Rick'

#f-strings

print(f'Name: {name}, Age: {age}')