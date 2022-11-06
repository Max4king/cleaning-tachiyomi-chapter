import re, os
from xmlrpc.client import Boolean

"""Prototype version that is the core concept"""
#   text = "test _ match this."
#   hi = re.findall("(?<=_).*", text)
#   print(hi)


def renameAllFiles(path):
    os.chdir(path)
    choose_char = input("purge till and '_'/ remove till 'C' or till custom character:")
    if choose_char == "_":
        for i in os.listdir(path):
            if i == "name-change.py":
                continue
            print(i)
            new_name = re.findall("(?<=_).*", i)
            if Boolean(new_name):
                name = new_name[0]
                print(name)
                os.rename(i, name)

    elif choose_char == "C":
        for i in os.listdir(path):
            if i == "name-change.py":
                continue
            print(i)
            new_name = re.findall("C.*", i)
            if Boolean(new_name):
                name = new_name[0]
                print(name)
                os.rename(i, name)
    else:
        if choose_char:
            for i in os.listdir(path):
                if i == "name-change.py":
                    continue
                print(i)
                choose_char  = choose_char + ".*"
                new_name = re.findall(choose_char, i)
                if Boolean(new_name):
                    name = new_name[0]
                    print(name)
                    os.rename(i, name)


def check_direct():
    if check_dir == "y":
        print(current_dir)
        path = current_dir
        confirm = input(f"{current_dir}\nAre you sure this is the correct directory(y/n):")
        if confirm == "y":
            quit()
        renameAllFiles(path)
    elif check_dir == "n":
        new_path_dir = input("Type the desired directory:")
        new_path_dir = new_path_dir.replace("\\","/")
        confirm = input(f"{current_dir}\nAre you sure this is the correct directory(y/n):")
        if confirm == "y":
            quit()
        renameAllFiles(path)
        print("Program quitting")
        quit()
    else:
        print("no directory selected! Program quit")


#default_dir = "/home/User/Documents/code/chapter2"
current_dir = os.getcwd()
check_dir = input("Do you want current_dir:(y/n):")
check_direct()
