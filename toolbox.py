#!/usr/bin/python3
# -*- coding: utf-8 -*-
import urllib.request
import time
import os
import string
import bz2
import gzip


def getPassDict(index):
    if (index >= 4):
        return FileExistsError
    url = [
        "https://github.com/danielmiessler/SecLists/blob/master/Passwords/Common-Credentials/10-million-password-list-top-1000000.txt",
        "http://downloads.skullsecurity.org/passwords/john.txt.bz2",
        "https://crackstation.net/files/crackstation-human-only.txt.gz",
        "http://downloads.skullsecurity.org/passwords/cain.txt.bz2"
    ]
    path = "files/passwords" + str(index) + ".txt"
    if not os.path.exists("files"):
        os.makedirs("files")
    try:
        f = open(path, 'r', encoding='raw_unicode_escape')
    except FileNotFoundError:
        print("Downloading a passwords list...")
        print("The file to be downloaded is :", url[index])

        if url[index].endswith('.gz'):
            extractedPath = "files/passwords" + str(index) + ".gz"
        elif url[index].endswith('.bz2'):
            extractedPath = "files/passwords" + str(index) + ".bz2"

        if (extractedPath):
            urllib.request.urlretrieve(url[index], extractedPath)
            print("Downloading Done")
            print("Proceeding to extract the file")
            extract(extractedPath, path)
            print("Successfully extracted the compressed file")
        else:
            urllib.request.urlretrieve(url[index], path)
            print("Downloading Done")

        f = open(path, 'r', encoding='raw_unicode_escape')
    passwords = []
    for password in f:
        passwords.append(password.strip())
    return passwords


def compareWithDict(userPassword, index):
    passwords = getPassDict(index)
    for password in passwords:
        if (userPassword == password):
            return False
    return True


def yesOrNo():
    answer = None
    while answer not in ("yes", "no"):
        answer = input("Enter yes or no: ")
        if answer == "yes":
            return True
        elif answer == "no":
            return False
        else:
            print("Please enter yes or no.")


def zeroOrOneOrTwo():
    answer = None
    while answer not in ("yes", "no"):
        answer = input("Enter yes or no: ")
        if answer == "1":
            return 1
        elif answer == "2":
            return 2
        elif answer == "3":
            return 3
        else:
            print("Please enter 0 or 1 or 2")


def welcome():
    print("Welcome to IsMyPswdSafe !")
    print(
        "This programs evaluates the quality of your password by comparing it to common passwords"
    )
    print("All is done in local, your password isn't stored.")
    print("This program may need an Internet access at the first start")
    print("Some password databases will be downloaded and it may take time")
    print(
        "Feel free to add other databases in order to make the test stronger")


def extract(compressedFile, newfile):
    print(compressedFile)
    if compressedFile.endswith('.gz'):
        inF = gzip.open(compressedFile, 'rb')
        s = inF.read()
        inF.close()
        with open(newfile, 'wb') as out_file:
            out_file.write(s)

    elif compressedFile.endswith('.bz2'):
        with open(newfile,
                  'wb') as new_file, bz2.BZ2File(compressedFile, 'rb') as file:
            for data in iter(lambda: file.read(100 * 1024), b''):
                new_file.write(data)
    else:
        print(
            "Type Of file not recognized. Please try a .bz2 or gzip compression"
        )
    return
