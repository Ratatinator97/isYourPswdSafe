#!/usr/bin/python3

import time
import sys
from toolbox import *

if __name__ == '__main__':
    welcome()
    print("Do you want to verify the setup ?")
    if (yesOrNo()):
        for i in range(4):
            getPassDict(i)
        print("Databases Downloaded Successfully \n the setup is DONE")
    print("Do you want a full review of the password quality ?")
    if (yesOrNo()):
        userPassword = input("Please type your password :")
        count = 0
        for i in range(4):
            if (not compareWithDict(userPassword, i)):
                count = count + 1
                print("The password has been found on the current database")
        print("The password has been found on " + str(count) + " databases")

        if (count != 0):
            print("Please change your password immediately")
            print(
                "Hint: Don't use a word you can find in the dictionnary, don't use names, things like replace 'e' with '3' are not very effective. Try to put at least 3 digits and two Caps."
            )
    print("Shutdown")
