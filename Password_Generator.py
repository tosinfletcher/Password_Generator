#       Program:                Password_Generator.py
#       Date:                   20/April/2020
#       Author:                 Oluwatosin Fletcher
#       Description:            This Program randomly generates a strong password


print("Password Generator".center(115))
print("**********************************************************************************************************************")
print("This Application Ask's you for a username of your choice and randomly generate a strong password for you.")
print("**********************************************************************************************************************")
                                          # If the User chooses option 2, perform the following task below.

while True:                                                         # Use a while loop along with a try and except to validate the users input.
    try:
        username = input("Please enter a username [No more than 20 characters in length]: ")            # Prompt the user to enter a username that is not more than 20 characters.
        if len(username) <1 or len(username) > 20:                                                      # If the lenght of the username is 0 and more than 20 prompt the user to enter the valid username
            print("The username is too long, please provide a username no more than 20 characters.")
            continue
        else:
            break

    except:
        print("Your username is too long, please provide a username no more than 20 characters.")


def RandomPasswordGen(RPD=True):                                                                        # Define a function called RandomPasswordGen to generate a list of random password

    from random import sample                                                                           # Import the sample function from random to help randomize the password
    lowerAlphabets = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m",
                          "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]                  # Create a list uppercase letter and store them in a variable called lowerAlphabets

    upperAlphabets = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M",
                          "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]                  # Create a list uppercase letter and store them in a variable called upperAlphabets

    Numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]                                        # Create a list of numbers and store them in a variable called Numbers
    Symbols = ["!", "+", "-", "=", "?", "#", "%", "*", "@", "&", "^", "_"]                              # Create a list of symbols and store them in a variable called Symbols

    UsernameAndRandPwd = []                                                                             # Create an empty list called UsernameAndRandPwd to store the user's username and randomly generated password.

    First_Ran_Num_Btw2and5 = sample([2, 4, 5], 1)                                                       # Use the sample function to generate a random number between 2 and 5
    Second_Ran_Num_Btw3and5 = sample([3, 4, 5], 1)                                                      # Use the sample function to generate a random number between 3 and 5
    Third_Ran_Num_Btw3and5 = sample([3, 4, 5], 1)                                                       # Use the sample function to generate a random number between 3 and 5
    Forth_Ran_Num_Btw3and5 = sample([3, 4, 5], 1)                                                       # Use the sample function to generate a random number between 3 and 5

    Total_of_Ran_Num_Btw2and5 = First_Ran_Num_Btw2and5[0] + Second_Ran_Num_Btw3and5[0] + Third_Ran_Num_Btw3and5[0] + Forth_Ran_Num_Btw3and5[0]          # Add the total number of randomly generated numbers together.

    lower = sample(lowerAlphabets, First_Ran_Num_Btw2and5[0])               # Use sample function to create a randlomly generated lowercase letters and use the first random number generated to determine how many lowercase letters will be generated.
    upper = sample(upperAlphabets, Second_Ran_Num_Btw3and5[0])              # Use sample function to create a randlomly generated uppercase letters and use the second random number generated to determine how many uppercase letters will be generated.
    num = sample(Numbers, Third_Ran_Num_Btw3and5[0])                        # Use sample function to create a randlomly generated numbers and use the third random number generated to determine how many numbers will be generated.
    sym = sample(Symbols, Forth_Ran_Num_Btw3and5[0])                        # Use sample function to create a randlomly generated symbols and use the forth random number generated to determine how many symblos will be generated.

    pwd = sample(lower + upper + num + sym, Total_of_Ran_Num_Btw2and5)      # Use the sample function to randomly create a password that totals the same amonut of randomly generated lowercase, uppercase, numbers and symbols.

    new_pwd = ""                                                            # Create an variable and set it to empty strings.
    for chr in pwd:                                                         # Use the for loop to loop through the randomly generated password
        new_pwd += chr                                                      # and save each character into the variable new_pwd as a set of string

    UsernameAndRandPwd.append(username)                                     # Save the username to the variable called UsernameAndRandPwd by appending it
    UsernameAndRandPwd.append(new_pwd + "\n")                               # Save the randomly generated password plus a new line to the variable called UsernameAndRandPwd by appending it
    print("----------------------------------------------------------------------------------------------------------------------")
    print("Your username is:", username)                                    # Output the username to the user
    print("Your password is:", new_pwd,"\n")                                     # Output the randomly generated password to the user
    print("----------------------------------------------------------------------------------------------------------------------")


    while True:                                                             # Use the while loop tho validate if the user would like to save their username and randomly generated password.
        savePwd = input("Would you like to save this username and password [Y/N]: ")                # Ask the user if they would like to save their username and randomly generated password
        savePwd = savePwd.upper()                                           # If the user enters a lowercase letter, covert it into an uppercase
        print("----------------------------------------------------------------------------------------------------------------------")

        if savePwd == True:                                                 # If the user input is true do nothing.
            pass

        elif savePwd == "Y" or savePwd == "YES":                            # If the user input is "Y" or "YES" break

            break

        elif savePwd == "N" or savePwd == "NO":                             # If the user input is "N" or "No" break

            break

        print("The correct format is [Y/N], Please try again")              # If the user input the wrong format for the input, tell the user what the correct format is and prompt them to type int the correct response.

    if savePwd == "Y" or savePwd == "YES":
        from os import strerror
        print("Note: If you do not enter a path, your file will be saved in the same directory you lunched the application from.")
        path = input("Please enter a path to save your new username and password, (Example = C:\\Users\\%USERNAME%\\Documents\\file.txt): ")  # Use the input function to ask the user for the path they would like to save their new username and password.
        print("----------------------------------------------------------------------------------------------------------------------")

        try:                                                                # Use the try and except along with the strerror to output the value of an error if it occurs
            if ".txt" not in path:                                          # If the user does not enter the a file extension add the extension ".txt"
                path += ".txt"

            stream = open(path, "at")                                       # Open path to append the username and randomly generated password to it.
            stream.writelines(",".join(UsernameAndRandPwd))                 # write the Username and Randomly generated password into the opened file while also using the join function.
            stream.close()                                                  # Close the stream.
            print("Your username and password has been saved successfully !\n")
            print("----------------------------------------------------------------------------------------------------------------------")
            print("This application is courtesy of: Oluwatosin Fletcher \n")

        except IOError as err:
            if strerror(err.errno) == "Permission denied":                                              # If IOError indicates permission denied, inform
                print("I/O error occurred:", strerror(err.errno))                                       # the user that the program has been terminated.
                print("You do not have permission to access this directory.\nProgram terminated!")      # and let them know they do not have access to the directory.
            else:
                print("I/O error occurred:", strerror(err.errno))
                print("Program terminated!")

    GenNewPwd2 = []                                                         # Create and emplty list called GenNewPwd2 to store the users response when asked if they would like to generate a new password.

    if savePwd == "N" or savePwd == "N0":                                   # If the User inputs "N" or "NO" when asked if they would like to save their password, perform the run the code within the while loop.
        while True:
            GenNewPwd = input("Would you like to generate a different password ? [Y/N]: ")          # Ask the user if they would like to generate a different password.
            GenNewPwd = GenNewPwd.upper()                                                           # If user response is a lowercase, covert it into an uppercase.
            GenNewPwd2.append(GenNewPwd)                                                            # Append the user's response into a the variable called GenNewPwd2

            if GenNewPwd == True:                                           # if the user's response is true do nothing
                pass
            elif GenNewPwd == "Y" or GenNewPwd == "YES":                    # If the user's response is "Y" or "YES" break
                break
            elif GenNewPwd == "N" or GenNewPwd == "NO":                     # If the user's response is "N" or "NO" print the courtesy statement below and break
                print()
                print("----------------------------------------------------------------------------------------------------------------------")
                print("This application is courtesy of: Oluwatosin Fletcher \n")
                break

            print("The correct format is [Y/N], Please try again")          # If the user input the wrong format for the input, tell the user what the correct format is and prompt them to type int the correct response.


    for k in GenNewPwd2:                                                    # Loop through the list GenNewPwd2 for the users input.
        if k == "Y" or k == "YES":                                          # If the user's input is "Y" or "YES", involke the
            RandomPasswordGen()                                             # RandomPasswordGen function to generate a new password.

RandomPasswordGen()

close = input("Press Enter to exit the application\n")                      # Allows users to close the application/program.
