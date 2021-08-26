'''Details:
For a given string s find the character c (or C) with longest consecutive repetition and return:

(c, l)
where l (or L) is the length of the repetition. If there are two or more characters with the same l return the first in
order of appearance.

For empty string return:

('', 0)
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------
My solution:
  '''

def longest_repetition(string):
    count = 0
    max_count = 0
    chars_list = []
    max_char = ''
    for i in range(len(string)):
        if string[i] not in chars_list:
            count = 0
            chars_list.append(string[i])
            count += 1
        else:
            if string[i] != string[i - 1]:
                count = 0
            count += 1

        if max_count < count:
            max_count = count
            max_char = string[i]

    if len(max_char) == 0:
        return ('', max_count)
    else:
        return (max_char, max_count)
