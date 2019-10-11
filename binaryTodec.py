number = int (input("Please Enter A Number In Decimal Form: "))
x = number
array = []
while (number > 0):
    b = int(float(number%2))
    array.append(b)
    number = (number - b) / 2
array.append(0)
string = ""
for c in array[::-1]:
    string = string + str(c)
print("The Binary Number for %d is %s"%(x, string))
