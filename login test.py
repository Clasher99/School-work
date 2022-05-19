counter = 0
username = input("Enter username")
password = input ("Enter password")
def login()
    locked = False
    loggedin = False
    while loggedin == False:
        while locked == False and counter < 2:
            if username == "Bob" and password == "Filip":
                loggedin = True
                print("Welcome to the Dice Game!")
                break
            else:
                print("Wrong username or password")
                username = input("Enter username")
                password = input("Enter password")

            if counter >= 3:
                print("Too many wrong attempts, bye")
                exit(code)

login()
print("Hi")