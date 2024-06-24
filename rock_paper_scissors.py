import random
myList=['rock','paper','scissors']
z=random.choice(myList)
user=input("Choose rock/paper/scissors:")
print(f"You chose {user}")
user=user.lower()
print(f"option chosen by system: {z}")
if z=='rock' and user=='paper':
    print("You won!")
elif z=='rock' and user=='scissors':
    print("You lose!")
elif z=='paper' and user=='rock':
    print("You lose!")
elif z=='paper' and user=='scissors':
    print("You won!")
elif z=='scissors' and user=='rock':
    print("You won!")
elif z=='scissors' and user=='paper':
    print("You lose!")
else:
    print("Tie match")
print("End of the match :)")