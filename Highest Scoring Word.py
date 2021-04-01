'''Details:
Given a string of words, you need to find the highest scoring word.

Each letter of a word scores points according to its position in the alphabet: a = 1, b = 2, c = 3 etc.

You need to return the highest scoring word as a string.

If two words score the same, return the word that appears earliest in the original string.

All letters will be lowercase and all inputs will be valid.

-------------------------------------------------------------------------------------------------------------------------------------------------------------------------
My solution:
'''
  def high(x):
    l = x.split()
    sum = 0
    max_sum = 0
    max_i = 0
    for i in l:
        sum = 0
        for j in i:
            simbol = ord(j)-96
            sum += simbol
        if sum > max_sum:
            max_sum = sum
            max_i = i
    return max_i
