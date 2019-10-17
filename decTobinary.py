decimal_str = input("Please Enter A Number In Bin Form: ")

decimal_str = decimal_str[::-1]

number = 0
i = 0

for a in decimal_str:
    number += int(a) * pow(2, i)
    i += 1

print ("Decimal is: ", number)