'''Details:
Complete the solution so that it strips all text that follows any of a set of comment markers passed in. Any whitespace at the end of the line should also be stripped out.

Example:

Given an input string of:

apples, pears # and bananas
grapes
bananas !apples
The output expected would be:

apples, pears
grapes
bananas
The code would be called like so:

result = solution("apples, pears # and bananas\ngrapes\nbananas !apples", ["#", "!"])
# result should == "apples, pears\ngrapes\nbananas"
------------------------------------------------------------------------------------------------------------------------------------------------------
My solution:
'''
def solution(string, markers):
    s = string.split('\n')
    for i,line in enumerate(s):
        for j in markers:
            index = line.find(j)
            if index != -1:
                line = line[:line.find(j)]
        s[i] = line.rstrip(' ')
    return '\n'.join(s)
