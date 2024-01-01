print('Welcome to my Elite 101 Chatbot!')
name = input('Please enter your name: ')
age = input(f' Hi {name}! How old are you? ')
print('Nice to meet you ' + name + '!' + f' Oh how to be {age} again!', end='') 
#end='' from StackOverflow 
# https://stackoverflow.com/questions/4390942/how-can-i-show-
# the-output-of-two-print-statements-on-the-same-line
print(' How can I help you today?') 

def chat_options():
  print('Please choose from the following speech options:')
  print('1. Placeholder Option 1 ') 
  print('2. Placeholder Option 2')    
  print('3. Placeholder Option 3')  
  print('4. Exit the conversation') 
chat_options()

def user_selection():
  user_choice = int(input('Please enter your numerical choice: '))
  if user_choice == 1: 
    print('\nPlaceholder Option 1')
  elif user_choice == 2:  
    print('\nPlaceholder Option 2') 
  elif user_choice == 3:  
    print('\nPlaceholder Option 3')
  elif user_choice == 4:  
    print(f'\nGoodbye {name}! have an awesome day!')
  else:
    print("Sorry, That's not a valid choice. Please input one of the numbers!")
user_selection()


