import re
def sum_of_integers_in_string(s):
    sum=0
    y=re.findall('[0-9]+',s) #this is a regular expression which means
                             #it will find all the numbers between 0-9
                             # + means, the numbers (0-9) can be repeated for 1 or multiple times
                             # y will be a list of all the numbers
    for i in range(len(y)):
        sum +=int(y[i])
    return sum