from random import randint


answer = randint(1, 100)
print(answer)

name = input("name?")
guess = input("guess num : ")

print(f'{name}, {guess}')

if ( guess == answer ):
    print("Congrats.")
else:
    print("Wrong.")
