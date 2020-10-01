'''
- Pascal's Triangle Redone
Author Enoch Oppong (D19126484)
Date 04/11/2019
'''
import string

def make_new_row(old_row):
    #Part A --> This section here uses the "append" function to add to the old row
    new_row = [1]
    for el in range(len(old_row)-1):
        new_row.append(old_row[el]+old_row[el+1])
    else:
        new_row.append(1)
    return new_row

    #Part B --> This section here starts the Pascal Triangle. When the array is null it returns a figure "1", when the old_row is updated it returns two more figures "1,1"
    if old_row == []:
        return [1]
    if old_row == [1]:
        return[1,1]

#This is the start of the Pascal Application. Its asks the user for a name and a number/integer
print("Welcome To The Pascal Application ^_^")
while True:
    try:
        yourName = input("What is your name? --> ")
        c = 0
        length = len(yourName)

        for el in yourName:
            if el in string.ascii_letters or el in string.whitespace:
                c += 1
        if c == length:
            break
        else:
            print("Invalid Input!")
    except ValueError:
        print("Please Enter A Proper Name!")
print("-----------------------------------")
enterName_str = print("Hello ",yourName,"!")
enterNum = input("Please Enter The Desired Height You Want Your Triangle To Be (Please Make Sure Number Is > 2 ) --> ")

#This while loop acts like the validation method of the Pascal Application. It checks to see if the user has entered the right values
while True:
    try:
        #This is converting the string into an integer
        numberEntered = int(enterNum)
    except:
        #Only numbers/integers can be entered
        enterNum = input("Error Only Numbers Please! --> ")
    else:
        #The number entered has to be greater than two!
        if numberEntered > 2:
            #This break here accepts the input given, only when greater than two!
            break
        else:
            enterNum = input("Please Enter A Bigger Number Than Two! --> ")

#This function "pascal_Triangle" is where the main action happens
def pascal_Triangle(numberEntered):
#These are my variables x and y. x prints out the first figure "1" which is at the start of the triangle. y is the list that will be append each time the height increases
    x = [[1]]
    y = [1,1]
    for alpha in range(numberEntered-2):
        x.append(y)
        y = make_new_row(y)
    else:
        x.append(y)

    #This print function is showing us the whole list of lists
    print()
    print("Here Is The Whole List of Lists! -->")
    print(x)
    print()

    #This print function is showing us a list of lists, printing one at a time
    print()
    print("Here Is The List Of Lists, Printing One List At A Time! --> ")
    for alpha in x:
        print(alpha)
    print()

    #Printing Triangle As A String
    print("Here Is The Lists As A Strings! --> ")
    for alpha in x:
        row = " ".join([str(tri) for tri in alpha])
        print(row.center(100))
pascal_Triangle(numberEntered)