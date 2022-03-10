import string, random

"""
Password generator project

use numbers, capitalcase and lowercase alpha letters, and special symbols

Input: password legnth

Output: The generatod password string

"""

def generate_password(password_length, include_spec_characters):
    lowercase_letters = [letter for letter in string.ascii_lowercase]
    uppercase_letters = [letter for letter in string.ascii_uppercase]
    digits = [digit for digit in string.digits]
    spec_chars = [char for char in string.punctuation]

    password = ""
    while len(password) < password_length:
        if include_spec_charaters:
            password += random.choice([random.choice(lowercase_letters),
                                    random.choice(spec_chars),
                                    random.choice(uppercase_letters), 
                                    random.choice(digits)])
        else: 
            password += random.choice([random.choice(lowercase_letters),
                        random.choice(uppercase_letters), 
                        random.choice(digits)])
    
    print ("Your generated password is  ------------>   {}".format(password))
    


if __name__ == "__main__":
    # Take some inputs from CLI
    print("Do you want use special characters in password generator ?")
    include_spec_charaters = input()
    if include_spec_charaters == "Yes" or include_spec_charaters == "":
        include_spec_charaters = True
    elif include_spec_charaters == "No":
        include_spec_charaters = False
    print("Enter the size of your password !!! \nThe defalt size is 5 characters !!!")
    try:
        password_length = int(input())
    except:
        password_length = 5

    print("Generating your password ... ")

    generate_password(password_length, include_spec_charaters)
