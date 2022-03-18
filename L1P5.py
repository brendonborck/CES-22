#PROBLEM 5

def is_palindrome(string):
    
    #middle = len(string)/2 + 1

    for i in range(len(string) - 1):

        if string[i] != string[len(string) - i - 1]:

            return False

    return True

