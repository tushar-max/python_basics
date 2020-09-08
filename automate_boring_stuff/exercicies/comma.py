"""
Write a function that takes a list value as an argument
and returns a string with all the items separated by a comma and a space, with and inserted before the last item.
"""

def coma_function(given_list):
    """
    Ill get the elemtents of the given_list and transform in to a string
    """
    string = ""
    for element in given_list[:len(given_list)-1]:
        string += element + ", "
    
    string += "and " + given_list[-1]
    
    return string

spam = ['apples', 'bananas', 'tofu', 'cats']

print(coma_function(spam))
# apples, bananas, tofu, and cats