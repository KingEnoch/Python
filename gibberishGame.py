#######################################################################################
# Program Description: Program that converts a word input by a user into gibberish and displays the gibberish word.
# Author: Thamsanqa Sibanda & Enoch Oppong
# Date: 07/10/2019
# Compiler: PyCharm Python 3.x
######################################################################################
import string
chkr = 2
repeat = ""
# Validation Variables
comp=0

# Loop to play game forever until user enters "no" to exit game.
while int(chkr) != 0:

    # if statement to check if game is continuing or is running for the first time and display the appropriate message
    if chkr == 2:
        # display intro message
        print(".....................................................\nWelcome to the \"Gibberish Word\" game.\n.....................................................")
        #print(".........................\nThe aim of this program is to enter translate English words to Gibberish!\n...................................")
    else:
        # reset chkr to 2 if game is repeating
        chkr = 2
        # Display message to notify user of new game
        print(".....................................................\nNew game has started.\n.....................................................")

    # Game code
    print("\nThis game's aim is to translate a user input word to \nGibberish using syllables that the user enters.")


    # prompt user for first syllable and perfom validation, i.e only letters and wildcard '*' allowed
    chkr2 = 0
    valid = 0
    while valid == 0:
        comp = 0
        if chkr2 == 0:
            input1 = input("\nEnter your first Gibberish syllable (add * for the vowel substitute): ")
            chkr2 = 1
        else:
            input1 = input("\nInvalid input!\nSyllable must only contain letters or a wildcard ('*'): ")

        # Validation code to check if a number is in the syllable
        for ltr in input1:
            if ltr == "*":
                comp += 1
            if ltr in string.ascii_letters:
                comp += 1
        if comp == len(input1):
            valid = 1
            # print("1")
        else:
            valid = 0
            # print("len = ", len(input1))
            # print(comp)

    input2 = input("Enter the second Gibberish syllable (* for vowel substitute): ")
    userword = input("Please enter a word you want to translate: ")

    # variables to check if a step has been executed. step1 will be used for the first syllable and step2 will be used for the second syllable
    step1 = 0
    step2 = 0
    gibWord = ""
    vows = "aeiouAEIOU"


    for ltr in userword:
        if ltr in vows:
            if step1 == 0:
                i = len(input1)
                if input1[0]=='*':
                    step1 += 1
                    input4 = ltr + input1[1:i]
                    gibWord = gibWord + input4
                    gibWord = gibWord + ltr
                else:
                    step1 += 1
                    gibWord = gibWord + input1
                    gibWord = gibWord + ltr
            else:
                i = len(input2)
                if input2[0] == '*':
                    input3 = ltr + input2[1:i]
                    gibWord = gibWord + input3
                    gibWord = gibWord + ltr
                else:
                    gibWord = gibWord + input2
                    gibWord = gibWord + ltr
        else:
            gibWord = gibWord + ltr
    print("........\nTranslated word is: ",gibWord,"\n........")

    while chkr != 0 and chkr != 1:
        # ask user if they want to continue playing the game.
        repeat = input("\nWould you like to continue playing the game(yes/no, y/n)? ")

        # code to exit game or continue playing.
        if repeat == "no" or repeat == "n":
            chkr = 0
            print(
                "\n.........................Game has ended....................... \n.....................Thank you for playing !..................")
        elif repeat == "yes" or repeat == "y":
            chkr = 1
        else:
            print("Invalid input, please enter a \"yes\"/\"y\" or \"no\"/\"n\"")

