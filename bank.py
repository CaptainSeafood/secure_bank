# The Bank
# Programmed by JDKim

# = User's usernames

## = Codes that need to be fixed

### = Code not in use

import sys
import time
import keyboard

instantConnect = input("")

if instantConnect:
    connecting = " "
    loading = " "
    # bar = "Connecting to server. . . . . . . . . . . . . . . . . . . . . . . . . . . "
    # bar = "Connecting to server .............................................................."
    bar = "Connecting to server... Connecting... Connecting... Connecting..."
    print(loading)
    for c in bar:
        time.sleep(0.09)
        sys.stdout.write(c)
        sys.stdout.flush()
    print(" ")
    bar = "!Server not responding!"
    print(loading)
    for c in bar:
        time.sleep(0.12)
        sys.stdout.write(c)
        sys.stdout.flush()
    print(" ")
    # bar = "Waiting for server......."
    bar = "Waiting for server... Waiting... Waiting..."
    print(loading)
    for c in bar:
        time.sleep(0.2)
        sys.stdout.write(c)
        sys.stdout.flush()
    print(" ")
    bar = "Server back online!"
    print(loading)
    for c in bar:
        time.sleep(0.1)
        sys.stdout.write(c)
        sys.stdout.flush()
    print(" ")
    bar = "Connected!"
    print(loading)
    for c in bar:
        time.sleep(0.01)
        sys.stdout.write(c)
        sys.stdout.flush()
    print(" ")
    # bar = "Loading..."
    # print(loading)
    # for c in bar:
    # time.sleep(0.01)
    # sys.stdout.write(c)
    # sys.stdout.flush()
    # print(" ")
    bar = "Opening in 1. 2. 3:"
    print(loading)
    for c in bar:
        time.sleep(0.2)
        sys.stdout.write(c)
        sys.stdout.flush()
else:
    print(" ")
print(" ")
print("--------------------------------------------------------------")
print("Updates:")
print(" ")
print("You are using v.12.4. Last updated 5/23/20 at 1:29:47 PST.")
print("--------------------------------------------------------------")
print("Sercurity:")
print(" ")
print("Here are the different levels of sercurity")
print("Level 1 = Just a password")
print("Level 2 = A password and a pin of your choice")
print("Level 3 = A password and a sercurity question")
print("Level 4 = A password, pin, and sercurity question")
print("--------------------------------------------------------------")
print("Bank:")
print(" ")
print("If you are here to see the bank here is the credentials:")
print("Username: All_Bank")
print("Password: THEBANK")
print("Pin: 0123456789")
print("--------------------------------------------------------------")
print("Account Checker:")
print(" ")
print("The account checker's account's credentials are:")
print("Username: Account_Check")
print("Password: ACCOUNT")
print("Pin: 0123456789")
print("--------------------------------------------------------------")
print("Programed by JDKim")
print("© 2020 Monster Tech and Codes")
print("Powered by trinket.io")
print("--------------------------------------------------------------")
bar = "Login:"
for c in bar:
    time.sleep(0.01)
    sys.stdout.write(c)
    sys.stdout.flush()
print(" ")
print(" ")
username = input("Please input your username:")
# Without Pin Level 1
if (username == "<Change>"):
    password = input("Please input your password:")
    if (password == "<Change>"):
        print(" ")
        print("You have ? tokens and ? credits")
    else:
        print(" ")
        print("Error! Code: Incorrect_Password. Reload the page to try again")
        print("  ")
        print("Disconnected from server")
# With Pin Level 2
elif (username == "<Change>"):
    password = input("Please input your password:")
    if (password == "<Change>"):
        pin = input("Please input your pin:")
        if (pin == "<Change>"):
            print(" ")
            print("You have ? tokens and ? credits")
        else:
            print(" ")
            print("Error! Code: Incorrect_Pin. Reload the page to try again")
            print("  ")
            print("Disconnected from server")
    else:
        print(" ")
        print("Error! Code: Incorrect_Password. Reload the page to try again")
        print("  ")
        print("Disconnected from server")
# With Sercurity Question Level 3
elif (username == "<Change>"):
    password = input("Please input your password:")
    if (password == "<Change>"):
        secrurequest = input("<Questiom>:")
        if (secrurequest == "<Change>"):
            print(" ")
            print("You have ? tokens and ? credits")
        else:
            print(" ")
            print("Error! Code: Incorrect_Answer. Reload the page to try again")
            print("  ")
            print("Disconnected from server")
    else:
        print(" ")
        print("Error! Code: Incorrect_Password. Reload the page to try again")
        print("  ")
        print("Disconnected from server")
# With Sercurity Question and pin Level 4
elif (username == "Test"):
    password = input("Please input your password:")
    if (password == "Test"):
        pin = input("Please input your pin:")
        if (pin == "Test"):
            secrurequest = input("<Question>:")
        if (secrurequest == "Test"):
            print(" ")
            print("You have ? tokens and ? credits")
        else:
            print(" ")
            print("Error! Code: Incorrect_Answer. Reload the page to try again")
            print("  ")
            print("Disconnected from server")
    else:
        print(" ")
        print("Error! Code: Incorrect_Password. Reload the page to try again")
        print("  ")
        print("Disconnected from server")
# User 1
elif (username == "User 1"):
    password = input("Please input your password:")
    if (password == "Password 1"):
        pin = input("Please input your pin:")
        if (pin == "Pin 1"):
            print(" ")
            print("You have ? tokens and ? credits")
        else:
            print(" ")
            print("Error! Code: Incorrect_Pin. Reload the page to try again")
            print("  ")
            print("Disconnected from server")
    else:
        print(" ")
        print("Error! Code: Incorrect_Password. Reload the page to try again")
        print("  ")
        print("Disconnected from server")
# User 2
elif (username == "User 2"):
    password = input("Please input your password:")
    if (password == "Password 2"):
        print(" ")
        print("You have ? tokens and ? credits")
    else:
        print(" ")
        print("Error! Code: Incorrect_Password. Reload the page to try again")
        print("  ")
        print("Disconnected from server")
# User 3
elif (username == "User 3"):
    password = input("Please input your password:")
    if (password == "Password 3"):
        print(" ")
        print("You have ? tokens and ? credits")
    else:
        print(" ")
        print("Error! Code: Incorrect_Password. Reload the page to try again")
        print("  ")
        print("Disconnected from server")
# User 4
elif (username == "User 4"):
    password = input("Please input your password:")
    if (password == "Password 4"):
        print(" ")
        print("You have ? tokens and ? credits")
    else:
        print(" ")
        print("Error! Code: Incorrect_Password. Reload the page to try again")
        print("  ")
        print("Disconnected from server")
# Mathy5
elif (username == "Mathy5"):
    password = input("Please input your password:")
    if (password == "Mathy5"):
        pin = input("Please input your pin:")
        if (pin == "Mathy5"):
            print(" ")
            print("You have 5 tokens and 34 credits")
        else:
            print(" ")
            print("Error! Code: Incorrect_Pin. Reload the page to try again")
            print("  ")
            print("Disconnected from server")
    else:
        print(" ")
        print("Error! Code: Incorrect_Password. Reload the page to try again")
        print("  ")
        print("Disconnected from server")
# MathWhiz143
elif (username == "MathWhiz143"):
    password = input("Please input your password:")
    if (password == "MEMEME"):
        secrurequest = input("What is your brothers name?:")
        if (secrurequest == "Josh"):
            print(" ")
            print("You have ? tokens and ? credits")
        else:
            print(" ")
            print("Error! Code: Incorrect_Answer. Reload the page to try again")
            print("  ")
            print("Disconnected from server")
    else:
        print(" ")
        print("Error! Code: Incorrect_Password. Reload the page to try again")
        print("  ")
        print("Disconnected from server")
# Bob143
elif (username == "Bob143"):
    password = input("Please input your password:")
    if (password == "Oh yeah"):
        pin = int(input("Please input your pin:"))
        if (pin == "65657"):
            print(" ")
            print("You have 44 tokens and 45 credits")
        else:
            print(" ")
            print("Error! Code: Incorrect_Pin. Reload the page to try again")
            print("  ")
            print("Disconnected from server")
    else:
        print(" ")
        print("Error! Code: Incorrect_Password. Reload the page to try again")
        print("  ")
        print("Disconnected from server")
# Jepal
elif (username == "Jepal"):
    password = input("Please input your password:")
    if (password == "JEpAL"):
        print(" ")
        print("You have 3 tokens and 23 credits")
    else:
        print(" ")
        print("Error! Code: Incorrect_Password. Reload the page to try again")
        print("  ")
        print("Disconnected from server")
# lizzykim
elif (username == "lizzykim"):
    password = input("Please input your password:")
    if (password == "Liz"):
        print(" ")
        print("You have 12 tokens and 24 credits")
        print("")
    else:
        print(" ")
        print("Error! Code: Incorrect_Password. Reload the page to try again")
        print("  ")
        print("Disconnected from server")
# Joeky_7
elif (username == "Joeky_7"):
    password = input("Please input your password:")
    if (password == "Oh"):
        print(" ")
        print("You have 4 tokens and 4 credits")
    else:
        print(" ")
        print("Error! Code: Incorrect_Password. Reload the page to try again")
        print("  ")
        print("Disconnected from server")
# JDKim
elif (username == "JDKim"):
    password = input("Please input your password:")
    if (password == "OH YES"):
        pin = input("Please input your pin:")
        if (pin == "6293"):
            secrurequest = input("Where did you first live in the US?:")
            if (secrurequest == "Denver"):
                print(" ")
                print("You have ∞ tokens and ∞ credits")
            else:
                print(" ")
                print("Error! Code: Incorrect_Answer. Reload the page to try again")
                print("  ")
                print("Disconnected from server")
        else:
            print(" ")
            print("Error! Code: Incorrect_Pin. Reload the page to try again")
            print("  ")
            print("Disconnected from server")
    else:
        print(" ")
        print("Error! Code: Incorrect_Password. Reload the page to try again")
        print("  ")
        print("Disconnected from server")
# Monster Level 10
elif (username == "Monster_Level10"):
    password = input("Please input your password:")
    if (password == "CODERED"):
        pin = input("Please input your pin:")
        if (pin == "1245"):
            secrurequest = input("What is the power-that-be's code name?:")
            if (secrurequest == "Mr.E"):
                print(" ")
                print("You have gained acess to a Level !10! database; here is data you need:")
                print(" ")
                print("Next meeting at 24:00:00 PST on 6/01/20.")
                print(" ")
                print("Next Targets for Level 10 agents:")
                print(" ")
                print("Agent Judo         |Juan Kuanj")
                print("Agent Fireblaze    |Kyle Rano")
                print("Agent Hawks        |Joey Fuller")
                print("Agent Momma        |Ben Operen Remi")
                print("Agent Jelly Legs   |Kyson Yanet Rang")
                print("Agent Green Runner |John Silver")
            else:
                print(" ")
                print("Error! Code: Incorrect_Answer. Reload the page to try again")
                print("  ")
                print("Disconnected from server")
        else:
            print(" ")
            print("Error! Code: Incorrect_Pin. Reload the page to try again")
            print("  ")
            print("Disconnected from server")
    else:
        print(" ")
        print("Error! Code: Incorrect_Password. Reload the page to try again")
        print("  ")
        print("Disconnected from server")
# Sunjung
elif (username == "drama977"):
    password = input("Please input your password:")
    if (password == "Love"):
        pin = input("Please input your pin:")
        if (pin == "6293"):
            secrurequest = input("Where did you first live in the US?:")
        if (secrurequest == "Denver"):
            print(" ")
            print("I love you!")
            print("I will give you my love. Ready? I LOVE YOU SO MUCH!!!!!!!!!!!!")
        else:
            print(" ")
            print("Error! Code: Incorrect_Answer. Reload the page to try again")
            print("  ")
            print("Disconnected from server")
    else:
        print(" ")
        print("Error! Code: Incorrect_Password. Reload the page to try again")
        print("  ")
        print("Disconnected from server")
# Shawn
elif (username == "renix6"):
    password = input("Please input your password:")
    if (password == "IAMAHAIRYMAN"):
        pin = input("Please input your pin:")
        if (pin == "6293"):
            secrurequest = input("Where did you first live in the US?:")
        if (secrurequest == "Denver"):
            print(" ")
            print("I love you!")
            print("I will give you my love. Ready? I LOVE YOU SO MUCH!!!!!!!!!!!!")
        else:
            print(" ")
            print("Error! Code: Incorrect_Answer. Reload the page to try again")
            print("  ")
            print("Disconnected from server")
    else:
        print(" ")
        print("Error! Code: Incorrect_Password. Reload the page to try again")
        print("  ")
        print("Disconnected from server")
# MathBannanaa12
elif (username == "MathBannanaa12"):
    password = input("Please input your password:")
    if (password == "MEME"):
        print(" ")
        print("You have 45 tokens and 43 credits")
    else:
        print(" ")
        print("Error! Code: Incorrect_Password. Reload the page to try again")
        print("  ")
        print("Disconnected from server")
# Bank
elif (username == "All_Bank"):
    password = input("Please input your password:")
    if (password == "THEBANK"):
        pin = input("Please input your pin:")
        if (pin == "0123456789"):
            print(" ")
            print("The Bank currently has 150 tokens and 3423 credits")
        else:
            print(" ")
            print("Error! Code: Incorrect_Pin. Reload the page to try again")
            print("  ")
            print("Disconnected from server")
    else:
        print(" ")
        print("Error! Code: Incorrect_Password. Reload the page to try again")
        print("  ")
        print("Disconnected from server")
# Account Checker
elif (username == "Account_Check"):
    password = input("Please input your password:")
    if (password == "ACCOUNT"):
        pin = input("Please input your pin:")
        if (pin == "0123456789"):
            print(" ")
            print("People with accounts are:")
            print(" ")
            print("Jepal          |PM            |Level 1 security")
            print("lizzykim       |PM            |Level 1 security")
            print("Joeky_7        |PM            |Level 1 security")
            print("MathBannanaa12 |PM            |Level 2 security")
            print("Bob154         |Gmail         |Level 2 security")
            print("MathWhiz143    |PM            |Level 3 security")
            print("Unknown        |Unknown       |Level 4 security")
            print("JDKim          |Default_Maker |Level 4 security")
        else:
            print(" ")
            print("Error! Code: Incorrect_Pin. Reload the page to try again")
            print("  ")
            print("Disconnected from server")
    else:
        print(" ")
        print("Error! Code: Incorrect_Password. Reload the page to try again")
        print("  ")
        print("Disconnected from server")
else:
    print(" ")
    print("Error! Code: Unknown_Username. Reload the page to try again.")
    print("  ")
    print("Disconnected from server")