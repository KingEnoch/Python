#!/usr/bin/python3

# Use the exchangeratesapi.io to perform currency conversions.
# https://api.exchangeratesapi.io/latest?base=EUR&symbols=USD

import urllib.request

VALID_CURRENCIES = ['USD', 'EUR', 'GBP', 'AUD', 'CAD',
                    'CNY', 'ILS', 'MXN', 'RUB', 'THB', 'BRL']


class Currency:
    def __init__(self, amount=1, currency_type='USD'):
        # a quick and easy way of checking for valid currencies
        # for a limited subset of valid currencies
        if currency_type in VALID_CURRENCIES:
            self.amount = amount
            self.currency_type = currency_type
        else:
            print("Invalid currency type: %s\n", currency_type)
            self.amount = 0
            self.currency_type = ''

    def convert_to(self, new_currency_type):
        if new_currency_type == self.currency_type:
            # nothing to do
            return Currency(self.amount, self.currency_type)

        if new_currency_type not in VALID_CURRENCIES or self.currency_type not in VALID_CURRENCIES:
            print("Converstion from %s to %s not allowed" % (self.currency_type, new_currency_type))
            return

        # prepare URL
        url = "https://api.exchangeratesapi.io/latest?base="
        url += self.currency_type
        url += "&symbols=" + new_currency_type
        # print(url)
        conv = urllib.request.urlopen(url)
        # read() returns an array of bytes, we want a string
        response = str(conv.read())

        # print (response)

        # begin breaking the string down into useful pieces
        left_index = response.index('{') + 1
        right_index = response.rindex('}')
        response = response[left_index:right_index]

        # split response into separate components
        resp_list = response.split(",")

        left_index = resp_list[0].index('{') + 1
        right_index = resp_list[0].rindex('}')
        exchange_rate = float(response[left_index:right_index].split(":")[1])

        # print(exchange_rate)
        amount = self.amount * exchange_rate

        print("%f %s => %f %s" % (self.amount, self.currency_type, amount, new_currency_type))
        return Currency(amount, new_currency_type)

    def __str__(self):
        return "%.2f %s" % (self.amount, self.currency_type)

    def __repr__(self):
        return self.__str__()

    def __add__(self, other_curr):
        if type(other_curr) is int or type(other_curr) is float:
            # no currency type specified, assume the same currency type
            new_amount = self.amount + other_curr
        else:
            if other_curr.currency_type != self.currency_type:
                # convert to current currency type
                other_curr = other_curr.convert_to(self.currency_type)
            # same currency type, nothing fancy needed
            new_amount = self.amount + other_curr.amount
        return Currency(new_amount, self.currency_type)

    def __sub__(self, other_curr):
        if type(other_curr) is int or type(other_curr) is float:
            # no currency type specified, assume the same currency type
            new_amount = self.amount - other_curr
        else:
            if other_curr.currency_type != self.currency_type:
                # convert to current currency type
                other_curr = other_curr.convert_to(self.currency_type)
            # same currency type, nothing fancy needed
            new_amount = self.amount - other_curr.amount
        # amounts less than 0 are allowed - you owe
        return Currency(new_amount, self.currency_type)

    def __radd__(self, other_curr):
        return self.__add__(other_curr)

    def __rsub__(self, other_curr):
        # note: subtraction is not commutative
        new_curr = Currency(other_curr, self.currency_type)
        return new_curr - self

    def __gt__(self, other_curr):
        if type(other_curr) is int or type(other_curr) is float:
            # no currency type specified, assume the same currency type
            result = self.amount > other_curr
        else:
            if other_curr.currency_type != self.currency_type:
                # convert to current currency type
                other_curr = other_curr.convert_to(self.currency_type)
            # same currency type, nothing fancy needed
            result = self.amount > other_curr.amount
        return result


# Main with a few examples calling the implemented methods
curr = Currency(7.50, 'USD')
print("Currency 1: ", end=" ")
print(curr)
curr2 = Currency(2, 'EUR')
print("Currency 2: ", end=" ")
print(curr2)
difference = curr - curr2
print("Currency 1 - Currency 2 = ", end=" ")
print(difference)
difference = curr2 - curr
print("Currency 2 - Currency 1 = ", end=" ")
print(difference)
print("5 - Currency 1 = ", end=" ")
print(5 - curr)
sum = curr + curr2
print("Currency 1 + Currency 2 = ", end=" ")
print(sum)
print("Currency 1 + 5.5 = ", end=" ")
print(curr + 5.5)
if curr > curr2:
    print ("Currency 1 greater than Currency 2")
else:
    print ("Currency 1 not greater than Currency 2")
