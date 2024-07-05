import random
import string

def generate_password(length, include_uppercase=True, include_symbols=True):
  
  char_list = [string.ascii_lowercase]
  if include_uppercase:
    char_list.append(string.ascii_uppercase)
  if include_symbols:
    char_list.append(string.punctuation)
  char_list.append(string.digits)  # Always include digits

  all_chars = ''.join(char_list)

  # Generate random password
  password = ''.join(random.choices(all_chars, k=length))
  return password

# Get user input for password length and character types (optional)
print("Welcome to password generator")
password_length = int(input("Enter desired password length : "))
include_uppercase = input("Include uppercase letters? (y/n): ").lower() == 'y'
include_symbols = input("Include symbols? (y/n): ").lower() == 'y'

# Generate password and print result
password = generate_password(password_length, include_uppercase, include_symbols)
print("Your generated password is:", password)
