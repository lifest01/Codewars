'''Details:
Implement the function unique_in_order which takes as argument a sequence and returns a list of items without any elements 
with the same value next to each other and preserving the original order of elements.

For example:

unique_in_order('AAAABBBCCDAABBB') == ['A', 'B', 'C', 'D', 'A', 'B']
unique_in_order('ABBCcAD')         == ['A', 'B', 'C', 'c', 'A', 'D']
unique_in_order([1,2,2,3,3])       == [1,2,3]

-------------------------------------------------------------------------------------------------------------------------------------------------------------------------
My solution:
'''
  def unique_in_order(iterable):
    string = []
    for i in range(len(iterable)):
        simbol = iterable[i]
        simbol2 = iterable[i - 1]
        if simbol != simbol2 or simbol not in string:
            string.append(simbol)
    return string
