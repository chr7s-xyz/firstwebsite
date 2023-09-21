import random

name = input("Enter your name :")
print('------------------')
print(f"Welcome {name} to Rock Paper  Scissors ! ")
print('------------------')


print("Please select one out of 'rock' 'paper' 'scissors'")
user_input = input('You select : ')
if user_input == 'rock':
 user_input='r'
elif user_input == 'paper':
 user_input='p'
elif user_input == 'scissors':
 user_input='s'
else :
 print('Invalid Option')
 
 
randNo = random.randint(1, 3) 

if randNo == 1:
    print('Computer selects : Rock')
    comp = 'r'

elif randNo == 2:
    print('Computer selects : paper')
    comp = 'p'

elif randNo == 3:
    print('Computer selects : scissor')
    comp = 's'

#We have got inputs : user_input and comp

if user_input == comp :
 print('Its a Draw, ',name)
#User choosing Rock : 
elif user_input == 'r':
 if comp == 'p':
  print('You lose, ',name)
 elif comp == 's':
   print('You win, ',name)
#User choosing Paper :
elif user_input == 'p':
 if comp == 's':
  print('You lose, ',name)
 elif comp == 'r':
   print('You win, ',name)
#User choosing Scissors :
elif user_input == 's':
 if comp == 'r':
  print('You lose, ',name)
 elif comp == 'p':
   print('You win, ',name)
   
print(f"Thanks for playing, {name} !")
print('------------------')
   

