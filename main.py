print('Welcome to my Elite 101 Chatbot!')
name = input('Please enter your name: ')
# from video https://docs.google.com/file/d/13j0cet_64kgzaYWH5bRooVS8U2HHMVfs/preview
age = input(f' Hi {name}! How old are you? ')
print('Nice to meet you ' + name + '!' + f' You\'re {age}? How young!', end='') 
#end='' from StackOverflow 
# https://stackoverflow.com/questions/4390942/how-can-i-show-
# the-output-of-two-print-statements-on-the-same-line
print(' How can I help you today?') 

def chat_options():
  print('Please choose from the following speech options:')
  print('1. What day is it today? ') 
  print('2. How are you?')    
  print('3. What do you like to do?')  
  print('4. Exit the conversation') 
chat_options()

def user_selection():
  user_choice = int(input('Please enter your numerical choice: '))
  if user_choice == 1: 
    print('\nDepends when you\'re asking me ;)')
  elif user_choice == 2:  
    print('\nFantastic, and you?') 
  elif user_choice == 3:  
    print('\nChat with you of course!')
  elif user_choice == 4:  
    print(f'\nGoodbye {name}! Talk to you later!')
  else:
    print("Sorry, That's not a valid choice. Please input one of the numbers!")
user_selection()


