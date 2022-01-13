print("**********\nUser Login\n**********\n")



sys_user_name = "akbalikadir"

sys_password  = "python"

right_of_entry = 3
while True:
    user_name = input("User Name: ")
    password = input("Password: ")

    if (user_name != sys_user_name and password == sys_password):
        print("Username is incorrect...")
        right_of_entry -= 1
        print("Remaining entry: ", right_of_entry)

    elif (user_name == sys_user_name and password != sys_password):
        print("Password is incorrect...")
        right_of_entry -= 1
        print("Remaining entry: ", right_of_entry)

    elif (user_name != sys_user_name and password != sys_password):
        print("Username and password are incorrect...")
        right_of_entry -= 1
        print("Remaining entry: ", right_of_entry)

    else:
        print("Successfully logged in...")
        break
    if (right_of_entry == 0 ):

        print("You have entered incorrectly too many times. That's why a reset link has been sent to your email account....")
        break




