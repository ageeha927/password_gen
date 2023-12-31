import random

def password(length):
    print('''
Hello! Welcome to your password generator.
          
Your password will include a combination of:
          
          uppercase letters, 
          lowercase letters, 
          numbers, and
          symbols in the generated passwords.

Well have fun!
          ''')
    letters = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
    'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D',
    'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S',
    'T', 'U', 'V', 'W', 'X', 'Y', 'Z'
    ]
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
    punctuation = ['!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', '-', '.', '/', ':', ';', '<', '=', '>', '?', '@', '[', '//', ']', '^', '_', '`', '{', '|', '}', '~']

    random.shuffle(letters)
    random.shuffle(numbers)
    random.shuffle(symbols)
    random.shuffle(punctuation)

    a = ''
    while a.lower() != 'exit':
        a = input('Would you like to continue? If not input exit.')
        if a.lower() != 'exit':
            length = input('What length would you like your password?(12 to 16)')
            if int(length) < 12:
                print("Your number should be at least 8.")
                a = input("Please, Enter your number again: ")
            else:
                one = round(int(length) * (30/100))
                two = round(int(length) * (20/100))
                password = []
                for x in range(one):
                    password.append(letters[x])
                    password.append(numbers[x])
                for x in range(two):
                    password.append(symbols[x])
                    password.append(punctuation[x])
                random.shuffle(password)
                password = "".join(password)
                return (f"Here is your password: {password}")
    

print(password(0))