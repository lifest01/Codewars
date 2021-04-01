'''Details:
Complete the method/function so that it converts dash/underscore delimited words into camel casing. 
The first word within the output should be capitalized only if the original word was capitalized (known as Upper Camel Case, also often referred to as Pascal case).

Examples:
"the-stealth-warrior" gets converted to "theStealthWarrior"
"The_Stealth_Warrior" gets converted to "TheStealthWarrior"

-------------------------------------------------------------------------------------------------------------------------------------------------------------------------
My solution:
  '''
  def to_camel_case(t):
    text=[]
    text.extend(t)
    t=text
    k = 0
    while k<len(text):
        if text[k]=='-' or text[k] == '_':
            text[k]=''
            text[k+1]=str.upper(text[k+1])
            k+=1
        k+=1
    return ''.join(t)
