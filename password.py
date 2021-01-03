import hashlib

hashed_password = ""
salt = "(?=gszAGG7"


def hash_it(password):
    salted_pwd = password + salt
    hashed_pass = hashlib.sha256(salted_pwd.encode('utf-8')).hexdigest()
    return hashed_pass


def check_password(pass1, pass2):
    if pass1 == pass2:
        print("Success! Your password has been registered.")
        return True
    else:
        print("Failed! Please try again...")
        return False


while True:
    ipt_pass1 = input("Type in a desired password: ")
    ipt_pass2 = input("One more time: ")

    if check_password(ipt_pass1, ipt_pass2):
        hashed_password = hash_it(ipt_pass1)
        break

print("Login:")
while True:
    if check_password(hash_it(input("Password: ")), hashed_password):
        print("Welcome to your home banking!")
        break
    else:
        print("Password failed. Please try again...")
