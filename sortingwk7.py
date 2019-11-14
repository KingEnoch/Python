'''
Week 7
OP Excerise --> Data Mining Stock Prices
Author --> Enoch Oppong
Date 14-11-2019
'''

#Data List Function
def get_data_list(file_name):
    data_file = open(file_name, "r")
    data_list = [ ] #Start with an empty list
    for line_str in data_file: #Strip end-of-line, split on commas, and append items to list
        data_list.append(line_str.strip().split(','))
    return data_list

