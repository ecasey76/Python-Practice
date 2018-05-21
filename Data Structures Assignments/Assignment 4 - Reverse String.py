# COP 4538 Assignment 4 - Reverse String
# By Eric Casey

# This program is O(n) complexity because the append method is an O(1)
# method and the counter decrement is O(1).
# When a string of size n is given as input,
# the append method will be called n times and the counter
# will be decremented n times.
# This means that the loop's complexity is 2n. This is O(n) because the
# constant 2 will become less significant when n is large.

# The other lines in the program outside of the loop
# are all constant time operations
# that don't significantly contribute to the complexity when n is large.

def reverseString(sentence):
    if sentence == "":
        return ""
    myList = list(sentence)
    revList = list()
    count = len(myList)-1
    while count >= 0:
        revList.append(myList[count])
        count -= 1
    return revList

def main():
    print("Enter a string: ")
    myString = input()
    print(reverseString(myString))

main()
