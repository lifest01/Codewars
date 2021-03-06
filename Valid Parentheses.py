'''Details:
Write a function that takes a string of parentheses, and determines if the order of the parentheses is valid. The function should return true if the string is valid, and false if it's invalid.

Examples
"()"              =>  true
")(()))"          =>  false
"("               =>  false
"(())((()())())"  =>  true

Constraints
0 <= input.length <= 100

-------------------------------------------------------------------------------------------------------------------------------------------------------------------------
My solution:
'''
def valid_parentheses(text):
    l = len(text)
    c = 0
    while len(text) > 0:
        a = text.find('(')
        b = text.find(')')
        if a == -1 and b == -1:
            break
        if (a < b and a != -1 and b != -1):
            text = text.replace('(', '', 1)
            text = text.replace(')', '', 1)
            c += 2
        else:
            return False

    if c % 2 == 0:
        return True
    else:
        return False
