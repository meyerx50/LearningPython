import hashlib
import sys
import random

# This will hold the final hashed password (plain + salt)
hashed_password = ""
# This is the salt for hashing the password
salt = ""
# How often can the user try registering or logging in
tries = 3
# This tracks if the user is already registered
registered = False
# Characters available for generating a salt

# Creates a salt based on the given length
def salt_it(length):
    return ''.join(chr(random.randint(33,126)) for i in range(length))

# Hashes a given password with the global set salt
def hash_it(password):
    salted_pwd = password + salt
    hashed_pass = hashlib.sha256(salted_pwd.encode('utf-8')).hexdigest()
    return hashed_pass

# Compare two given passwords
def check_password(pass1, pass2):
    if pass1 == pass2:
        print("Success! Your password has been registered.")
        return True
    else:
        print("Failed! Passwords must match")
        return False

# Offers the user the chance to register his/her password
for x in range(tries):
    ipt_pass1 = input("Type in a desired password: ")
    ipt_pass2 = input("One more time: ")

    if check_password(ipt_pass1, ipt_pass2):
        salt = salt_it(16)
        hashed_password = hash_it(ipt_pass1 + salt)
        registered = True
        break

# Did the user successfully registered?
if registered:
    # If so, let's now login
    print("Please login...")
    # Give him/her a pre-determined number of chances
    for x in range(tries):
        # Correct password?
        if check_password(hash_it(input("Password: ") + salt), hashed_password):
            print("Welcome to your home banking!")
            break
        else:
            # Try again
            if x+1 < tries:
                print("Password failed. Please try again...")
            # Too many times? Bye!
            else:
                print("We are sorry you are not able to login. Please call our hotline!")
                sys.exit()
else:
    print("We are sorry you are not able to login. Please call our hotline!")
    sys.exit()
