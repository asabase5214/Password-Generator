import random

#Put all the contents of adjectives.txt in a list called adjectives
with open('adjectives.txt', 'r') as file:
  file_content = file.read()
adjectives = file_content.splitlines()

#Put all the contents of nouns.txt in a list called nouns
with open('nouns.txt', 'r') as file:
  file_content = file.read()
nouns = file_content.splitlines()

alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
#Use the list alphabet to create a list of the alphabet in lower case
lower_alpha = []
for i in range(len(alphabet)):
  lower_alpha.append(alphabet[i].lower())

nums = ['1', '2', '3', '4', '5', '6', '7', '8', '9']

symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+', '/', '\\', '|', '}', '{', '~', '`', '[', ']', '^', '_', '-', ':', ';', '<', '=', '>', '?', '@', '.', ',', '%']

#Coombine alphabet, lower_alpha, nums, and symbols in a larger list called allCharacters (repeats alphabet and lower_alpha so that they would be more likely to appear in a password than numbers and symbols)
allCharacters = alphabet+alphabet+alphabet+lower_alpha+lower_alpha+lower_alpha+nums+symbols

#Ask user what password they want (backslash t for a new tab, to make it easier to read)
type = input('What type of password do you want: a PIN (1), \tan adjective-noun password (one that will be possible to memorize) (2), \tor a randomly generated password (not easily memorized, but secure) (3)? ')

#If the user wanted a PIN
if type == '1':
  #Ask user how long they want the PIN
  length = input('Enter the amount of numbers you want your PIN to include: ')
  #Use a loop to make sure the user enters a number
  while True:
    if not length.isdigit():
      print('Please enter a number.')
      length = input()
    else:
      length = int(length)
      break
  #l1 is the variable that will be the first parameter in the randint funtion later
  l1_1 = '1'
  l1_2 = '0'*(length-1)
  l1 = l1_1 + l1_2
  l1 = int(l1)
  #l2 is the second parameter
  l2 = int('9'*length)
  #print and generate the PIN
  print('Your PIN is ' + str(random.randint(l1, l2)))

#If the user wanted a password that can be memorized easily
elif type == '2':
  print('You password is ' + random.choice(adjectives) + random.choice(nouns) + str(random.randint(100,999)))

#If the user wanted a completely random password
elif type == '3':
  length = random.randint(8, 15)
  password = []
  #Make a list of each individual character in the password
  for i in range(length):
    password.append(random.choice(allCharacters))
  #Print the list one character at a time, using the end="" to ensure that the password will be on one single line
  for i in range(len(password)):
    print(password[i], end="")